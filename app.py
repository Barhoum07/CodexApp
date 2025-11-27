from flask import Flask, render_template, request, jsonify
from content import curriculum
import json
import os

app = Flask(__name__)
PROGRESS_FILE = 'progress.json'

# Helper to flatten missions for easy access
def get_all_missions():
    missions = []
    for module_key, module in curriculum.items():
        for mission in module['missions']:
            mission['module_title'] = module['title']
            mission['module_id'] = module_key
            missions.append(mission)
    return missions

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return []
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_progress(mission_id):
    progress = load_progress()
    if mission_id not in progress:
        progress.append(mission_id)
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f)

@app.route('/')
def index():
    all_missions = get_all_missions()
    completed_missions = load_progress()
    
    # Determine status for each mission
    # Logic: 
    # - If mission_id in completed_missions -> 'completed'
    # - The first mission NOT in completed_missions -> 'active'
    # - All subsequent missions -> 'locked'
    
    active_found = False
    
    for mission in all_missions:
        if mission['id'] in completed_missions:
            mission['status'] = 'completed'
        elif not active_found:
            mission['status'] = 'active'
            active_found = True
        else:
            mission['status'] = 'locked'
            
    return render_template('index.html', missions=all_missions, curriculum=curriculum)

@app.route('/mission/<mission_id>')
def mission(mission_id):
    all_missions = get_all_missions()
    mission_data = next((m for m in all_missions if m['id'] == mission_id), None)
    
    if not mission_data:
        return "Mission not found", 404
        
    # Check if mission is accessible
    # It must be completed OR the current active mission
    # We can reuse the logic from index() or just check if previous mission is completed
    
    completed_missions = load_progress()
    current_index = all_missions.index(mission_data)
    
    # If it's the first mission, it's always accessible
    if current_index == 0:
        pass
    # If it's not the first, the previous mission must be completed
    else:
        prev_mission = all_missions[current_index - 1]
        if prev_mission['id'] not in completed_missions and mission_data['id'] not in completed_missions:
             # If previous not completed AND this one not completed (meaning not revisited), block it
             # But wait, if I completed mission 1, mission 2 is active. 
             # So if mission 2 is requested, mission 1 must be in completed_missions.
             return "Access Denied: Level Locked", 403

    # Find next mission
    next_mission = all_missions[current_index + 1] if current_index + 1 < len(all_missions) else None
    
    return render_template('mission.html', mission=mission_data, next_mission=next_mission)

@app.route('/check_code', methods=['POST'])
def check_code():
    data = request.json
    code = data.get('code', '')
    mission_id = data.get('mission_id')
    
    all_missions = get_all_missions()
    mission_data = next((m for m in all_missions if m['id'] == mission_id), None)
    
    if not mission_data:
        return jsonify({'success': False, 'message': 'Mission not found'})
    
    # Enhanced keyword validation (Case Insensitive)
    keywords = mission_data.get('validation_keywords', [])
    # Normalize code to lowercase for validation
    code_lower = code.lower()
    
    missing = []
    for kw in keywords:
        # Check if keyword is in code (case insensitive)
        if kw.lower() not in code_lower:
            missing.append(kw)
    
    if not missing:
        save_progress(mission_id)
        return jsonify({'success': True, 'message': 'System Override Successful. Access Granted.'})
    else:
        return jsonify({'success': False, 'message': f'Validation Failed. Missing sequences: {", ".join(missing)}'})

if __name__ == '__main__':
    app.run(debug=True)
