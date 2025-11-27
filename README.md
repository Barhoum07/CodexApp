# CodeNexus - Interactive Web Learning Platform

An interactive learning platform for HTML, CSS, and JavaScript with 77 progressive missions and 20 challenges.

## Features
- 🎯 11 HTML levels
- 🎨 18 CSS levels  
- 💻 28 JavaScript levels
- 🏆 20 progressive challenges (Easy → Medium → Hard)
- 🔒 Level locking system with progress tracking
- 📝 Interactive code editor with live preview

## Local Development

### Prerequisites
- Python 3.8+

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd codexapp

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

## Deployment

### Deploy to Render
1. Push code to GitHub
2. Create account at [render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Deploy!

### Deploy to Railway
1. Push code to GitHub
2. Sign up at [railway.app](https://railway.app)
3. Create new project from GitHub repo
4. Railway auto-detects and deploys

## Project Structure
```
codexapp/
├── app.py              # Flask application
├── content.py          # Curriculum content
├── progress.json       # User progress tracking
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   └── mission.html
└── static/            # CSS, JS, assets
    ├── style.css
    └── script.js
```

## License
MIT License
