# content.py

curriculum = {
    "html": {
        "title": "Module 1: The Skeleton (HTML5)",
        "description": "Forge the structure of the web. Learn the tags that bind the digital world.",
        "missions": [
            # Level 1: HTML Foundations
            {
                "id": "html_foundations",
                "title": "Level 1: HTML Foundations",
                "description": "Build the core structure of every web page.",
                "content": """
                    <h3>HTML Foundations</h3>
                    <p><strong>&lt;html&gt;</strong>: The root element that wraps all content.</p>
                    <p><strong>&lt;head&gt;</strong>: Contains metadata about the document.</p>
                    <p><strong>&lt;body&gt;</strong>: Contains all visible content.</p>
                """,
                "task": "Create a complete HTML document with html, head, and body tags.",
                "hint": "Start with <html>, nest <head> and <body> inside it.",
                "starter_code": "<!-- Create HTML structure -->\n",
                "validation_keywords": ["<html", "<head", "<body", "</html>", "</head>", "</body>"]
            },
            
            # Level 2: Titles & Paragraphs
            {
                "id": "html_titles_paragraphs",
                "title": "Level 2: Titles & Paragraphs",
                "description": "Add headings and text content.",
                "content": """
                    <h3>Headings and Paragraphs</h3>
                    <p><strong>&lt;h1&gt; to &lt;h6&gt;</strong>: Heading tags from most to least important.</p>
                    <p><strong>&lt;p&gt;</strong>: Paragraph tag for text blocks.</p>
                """,
                "task": "Create an h1 heading, an h2 heading, and a paragraph.",
                "hint": "<h1>Main Title</h1><h2>Subtitle</h2><p>Text</p>",
                "starter_code": "<body>\n  <!-- Add headings and paragraph -->\n</body>",
                "validation_keywords": ["<h1", "<h2", "<p", "</h1>", "</h2>", "</p>"]
            },
            
            # Level 3: Text Structuring
            {
                "id": "html_text_structure",
                "title": "Level 3: Text Structuring",
                "description": "Format and emphasize text.",
                "content": """
                    <h3>Text Formatting</h3>
                    <p><strong>&lt;strong&gt;</strong>: Bold/important text.</p>
                    <p><strong>&lt;em&gt;</strong>: Italic/emphasized text.</p>
                    <p><strong>&lt;br&gt;</strong>: Line break.</p>
                    <p><strong>&lt;hr&gt;</strong>: Horizontal rule/divider.</p>
                """,
                "task": "Create a paragraph with bold text, italic text, and a line break.",
                "hint": "<p>Normal <strong>bold</strong> <em>italic</em><br>new line</p>",
                "starter_code": "<p>\n  <!-- Add formatted text -->\n</p>",
                "validation_keywords": ["<strong", "<em", "<br", "</strong>", "</em>"]
            },
            
            # Level 4: Lists
            {
                "id": "html_lists",
                "title": "Level 4: Lists",
                "description": "Organize items in lists.",
                "content": """
                    <h3>Lists</h3>
                    <p><strong>&lt;ul&gt;</strong>: Unordered (bulleted) list.</p>
                    <p><strong>&lt;ol&gt;</strong>: Ordered (numbered) list.</p>
                    <p><strong>&lt;li&gt;</strong>: List item.</p>
                """,
                "task": "Create both an unordered list and an ordered list, each with at least 2 items.",
                "hint": "<ul><li>Item</li></ul> and <ol><li>Item</li></ol>",
                "starter_code": "<!-- Create lists -->\n",
                "validation_keywords": ["<ul", "<ol", "<li", "</ul>", "</ol>", "</li>"]
            },
            
            # Level 5: Videos
            {
                "id": "html_videos",
                "title": "Level 5: Videos",
                "description": "Embed video content.",
                "content": """
                    <h3>Video Element</h3>
                    <p><strong>&lt;video&gt;</strong>: Embeds a video file.</p>
                    <p><strong>src</strong>: Source file path.</p>
                    <p><strong>controls</strong>: Shows play/pause controls.</p>
                """,
                "task": "Embed a video with src='video.mp4' and controls.",
                "hint": "<video src='video.mp4' controls></video>",
                "starter_code": "<!-- Add video -->\n",
                "validation_keywords": ["<video", "src=", "controls", "</video>"]
            },
            
            # Level 6: Semantic Tags
            {
                "id": "html_semantic",
                "title": "Level 6: Semantic Tags",
                "description": "Structure pages with meaning.",
                "content": """
                    <h3>Semantic HTML</h3>
                    <p><strong>&lt;header&gt;</strong>: Page or section header.</p>
                    <p><strong>&lt;nav&gt;</strong>: Navigation links.</p>
                    <p><strong>&lt;section&gt;</strong>: Thematic grouping of content.</p>
                    <p><strong>&lt;footer&gt;</strong>: Page or section footer.</p>
                """,
                "task": "Create a page layout with header, nav, section, and footer.",
                "hint": "<header><nav></nav></header><section></section><footer></footer>",
                "starter_code": "<body>\n  <!-- Add semantic structure -->\n</body>",
                "validation_keywords": ["<header", "<nav", "<section", "<footer"]
            },
            
            # Level 7: Links
            {
                "id": "html_links",
                "title": "Level 7: Links",
                "description": "Connect pages together.",
                "content": """
                    <h3>Hyperlinks</h3>
                    <p><strong>&lt;a&gt;</strong>: Anchor tag for links.</p>
                    <p><strong>href</strong>: URL destination.</p>
                    <p><strong>target="_blank"</strong>: Opens in new tab.</p>
                """,
                "task": "Create a link to 'https://example.com' with text 'Visit Example'.",
                "hint": "<a href='https://example.com'>Visit Example</a>",
                "starter_code": "<!-- Create link -->\n",
                "validation_keywords": ["<a", "href=", "</a>"]
            },
            
            # Level 8: Images
            {
                "id": "html_images",
                "title": "Level 8: Images",
                "description": "Display images on your page.",
                "content": """
                    <h3>Images</h3>
                    <p><strong>&lt;img&gt;</strong>: Image element (self-closing).</p>
                    <p><strong>src</strong>: Image file path.</p>
                    <p><strong>alt</strong>: Alternative text description.</p>
                """,
                "task": "Add an image with src='logo.png' and alt='Company Logo'.",
                "hint": "<img src='logo.png' alt='Company Logo'>",
                "starter_code": "<!-- Add image -->\n",
                "validation_keywords": ["<img", "src=", "alt="]
            },
            
            # Level 9: Forms
            {
                "id": "html_forms",
                "title": "Level 9: Forms",
                "description": "Collect user input.",
                "content": """
                    <h3>Forms</h3>
                    <p><strong>&lt;form&gt;</strong>: Form container.</p>
                    <p><strong>&lt;input&gt;</strong>: Input field (type: text, email, password, etc.).</p>
                    <p><strong>&lt;label&gt;</strong>: Label for inputs.</p>
                    <p><strong>&lt;button&gt;</strong>: Submit button.</p>
                """,
                "task": "Create a form with a text input, an email input, and a submit button.",
                "hint": "<form><input type='text'><input type='email'><button>Submit</button></form>",
                "starter_code": "<!-- Create form -->\n",
                "validation_keywords": ["<form", "<input", "type=", "<button", "</form>"]
            },
            
            # Level 10: Tables
            {
                "id": "html_tables",
                "title": "Level 10: Tables",
                "description": "Display data in rows and columns.",
                "content": """
                    <h3>Tables</h3>
                    <p><strong>&lt;table&gt;</strong>: Table container.</p>
                    <p><strong>&lt;tr&gt;</strong>: Table row.</p>
                    <p><strong>&lt;th&gt;</strong>: Table header cell.</p>
                    <p><strong>&lt;td&gt;</strong>: Table data cell.</p>
                """,
                "task": "Create a table with a header row and 2 data rows.",
                "hint": "<table><tr><th>Name</th></tr><tr><td>John</td></tr></table>",
                "starter_code": "<!-- Create table -->\n",
                "validation_keywords": ["<table", "<tr", "<th", "<td", "</table>"]
            },
            
            # Level 11: Div & Span
            {
                "id": "html_div_span",
                "title": "Level 11: Div & Span",
                "description": "Generic containers for styling.",
                "content": """
                    <h3>Containers</h3>
                    <p><strong>&lt;div&gt;</strong>: Block-level container (takes full width).</p>
                    <p><strong>&lt;span&gt;</strong>: Inline container (only takes needed space).</p>
                """,
                "task": "Create a div containing multiple span elements.",
                "hint": "<div><span>Text 1</span> <span>Text 2</span></div>",
                "starter_code": "<!-- Create containers -->\n",
                "validation_keywords": ["<div", "<span", "</div>", "</span>"]
            }
        ]
    },
    
    "css": {
        "title": "Module 2: The Skin (CSS3)",
        "description": "Style the construct. Manipulate the visual presentation.",
        "missions": [
            # Level 1: CSS Rules
            {
                "id": "css_rules",
                "title": "Level 1: CSS Rules",
                "description": "Learn CSS syntax and selectors.",
                "content": """
                    <h3>CSS Syntax</h3>
                    <p>CSS rules: <code>selector { property: value; }</code></p>
                    <p><strong>Element selector</strong>: p { }</p>
                    <p><strong>Class selector</strong>: .classname { }</p>
                    <p><strong>ID selector</strong>: #idname { }</p>
                """,
                "task": "Write a CSS rule to make all paragraphs red.",
                "hint": "p { color: red; }",
                "starter_code": "<style>\n  /* Add CSS rule */\n</style>\n<p>Text</p>",
                "validation_keywords": ["p", "{", "color:", "red", "}"]
            },
            
            # Level 2: Text Formatting Part 1
            {
                "id": "css_text_1",
                "title": "Level 2: Text Formatting (Part 1)",
                "description": "Color, font family, and size.",
                "content": """
                    <h3>Text Properties</h3>
                    <p><strong>color</strong>: Text color.</p>
                    <p><strong>font-family</strong>: Font type (Arial, sans-serif, etc.).</p>
                    <p><strong>font-size</strong>: Text size (px, rem, em).</p>
                """,
                "task": "Style text with color blue, font-family Arial, and font-size 18px.",
                "hint": "p { color: blue; font-family: Arial; font-size: 18px; }",
                "starter_code": "<style>\n  p {\n    /* Add styles */\n  }\n</style>\n<p>Styled text</p>",
                "validation_keywords": ["color:", "font-family:", "font-size:"]
            },
            
            # Level 3: Text Formatting Part 2
            {
                "id": "css_text_2",
                "title": "Level 3: Text Formatting (Part 2)",
                "description": "Alignment and decoration.",
                "content": """
                    <h3>More Text Properties</h3>
                    <p><strong>text-align</strong>: left, center, right, justify.</p>
                    <p><strong>text-decoration</strong>: underline, none, line-through.</p>
                    <p><strong>text-transform</strong>: uppercase, lowercase, capitalize.</p>
                """,
                "task": "Center align text, remove underline, and make it uppercase.",
                "hint": "text-align: center; text-decoration: none; text-transform: uppercase;",
                "starter_code": "<style>\n  p {\n    /* Add styles */\n  }\n</style>\n<p>Text</p>",
                "validation_keywords": ["text-align:", "center", "text-decoration:", "text-transform:"]
            },
            
            # Level 4: Borders
            {
                "id": "css_borders",
                "title": "Level 4: Borders",
                "description": "Add borders to elements.",
                "content": """
                    <h3>Border Properties</h3>
                    <p><strong>border</strong>: Shorthand (width style color).</p>
                    <p><strong>border-radius</strong>: Rounded corners.</p>
                    <p>Example: border: 2px solid black;</p>
                """,
                "task": "Create a box with a solid border and rounded corners.",
                "hint": "div { border: 2px solid black; border-radius: 10px; }",
                "starter_code": "<style>\n  div {\n    width: 100px;\n    height: 100px;\n    /* Add border styles */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["border:", "border-radius:"]
            },
            
            # Level 5: Margins
            {
                "id": "css_margins",
                "title": "Level 5: Margins & Padding",
                "description": "Control spacing around and inside elements.",
                "content": """
                    <h3>Box Model</h3>
                    <p><strong>margin</strong>: Space outside the border.</p>
                    <p><strong>padding</strong>: Space inside the border.</p>
                    <p>Can specify: margin: 10px; or margin: 10px 20px; (top/bottom left/right)</p>
                """,
                "task": "Add 20px margin and 15px padding to an element.",
                "hint": "div { margin: 20px; padding: 15px; }",
                "starter_code": "<style>\n  div {\n    border: 1px solid;\n    /* Add spacing */\n  }\n</style>\n<div>Box</div>",
                "validation_keywords": ["margin:", "padding:"]
            },
            
            # Level 6: List Formatting
            {
                "id": "css_lists",
                "title": "Level 6: List Formatting",
                "description": "Style list appearance.",
                "content": """
                    <h3>List Styles</h3>
                    <p><strong>list-style-type</strong>: disc, circle, square, none.</p>
                    <p><strong>list-style-position</strong>: inside, outside.</p>
                """,
                "task": "Remove bullets from a list.",
                "hint": "ul { list-style-type: none; }",
                "starter_code": "<style>\n  ul {\n    /* Style list */\n  }\n</style>\n<ul><li>Item</li></ul>",
                "validation_keywords": ["list-style-type:", "none"]
            },
            
            # Level 7: Backgrounds
            {
                "id": "css_backgrounds",
                "title": "Level 7: Backgrounds",
                "description": "Set background colors and images.",
                "content": """
                    <h3>Background Properties</h3>
                    <p><strong>background-color</strong>: Solid color.</p>
                    <p><strong>background-image</strong>: url('image.jpg').</p>
                    <p><strong>background-size</strong>: cover, contain, or dimensions.</p>
                """,
                "task": "Set a background color and background image.",
                "hint": "div { background-color: lightblue; background-image: url('bg.jpg'); }",
                "starter_code": "<style>\n  div {\n    width: 200px;\n    height: 200px;\n    /* Add background */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["background-color:", "background-image:"]
            },
            
            # Level 8: Filters
            {
                "id": "css_filters",
                "title": "Level 8: Filters",
                "description": "Apply visual effects.",
                "content": """
                    <h3>CSS Filters</h3>
                    <p><strong>filter</strong>: Apply effects to elements.</p>
                    <p><strong>blur()</strong>: Blur effect (px).</p>
                    <p><strong>grayscale()</strong>: Convert to grayscale (0-1 or %).</p>
                    <p><strong>brightness()</strong>, <strong>contrast()</strong>: Adjust levels.</p>
                """,
                "task": "Apply blur and grayscale filters to an image.",
                "hint": "img { filter: blur(2px) grayscale(50%); }",
                "starter_code": "<style>\n  img {\n    /* Add filters */\n  }\n</style>\n<img src='photo.jpg' alt='Photo'>",
                "validation_keywords": ["filter:", "blur", "grayscale"]
            },
            
            # Level 9: Table Formatting
            {
                "id": "css_tables",
                "title": "Level 9: Table Formatting",
                "description": "Style tables.",
                "content": """
                    <h3>Table Styles</h3>
                    <p><strong>border-collapse</strong>: collapse (single borders) or separate.</p>
                    <p><strong>border-spacing</strong>: Space between cells (if separate).</p>
                """,
                "task": "Style a table with collapsed borders.",
                "hint": "table { border-collapse: collapse; } td { border: 1px solid; }",
                "starter_code": "<style>\n  table {\n    /* Style table */\n  }\n  td {\n    /* Style cells */\n  }\n</style>\n<table><tr><td>Cell</td></tr></table>",
                "validation_keywords": ["border-collapse:", "border:"]
            },
            
            # Level 10: Transforms - Translate
            {
                "id": "css_translate",
                "title": "Level 10: Transforms - Translate",
                "description": "Move elements.",
                "content": """
                    <h3>Transform: Translate</h3>
                    <p><strong>transform: translate(x, y)</strong>: Move element.</p>
                    <p><strong>translateX()</strong>: Move horizontally.</p>
                    <p><strong>translateY()</strong>: Move vertically.</p>
                """,
                "task": "Move an element 50px right and 30px down.",
                "hint": "div { transform: translate(50px, 30px); }",
                "starter_code": "<style>\n  div {\n    width: 100px;\n    height: 100px;\n    background: red;\n    /* Add transform */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["transform:", "translate"]
            },
            
            # Level 11: Transforms - Rotate
            {
                "id": "css_rotate",
                "title": "Level 11: Transforms - Rotate",
                "description": "Rotate elements.",
                "content": """
                    <h3>Transform: Rotate</h3>
                    <p><strong>transform: rotate(deg)</strong>: Rotate element.</p>
                    <p>Positive values: clockwise. Negative: counter-clockwise.</p>
                """,
                "task": "Rotate an element 45 degrees.",
                "hint": "div { transform: rotate(45deg); }",
                "starter_code": "<style>\n  div {\n    width: 100px;\n    height: 100px;\n    background: blue;\n    /* Add rotation */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["transform:", "rotate", "45deg"]
            },
            
            # Level 12: Transforms - Scale
            {
                "id": "css_scale",
                "title": "Level 12: Transforms - Scale",
                "description": "Resize elements.",
                "content": """
                    <h3>Transform: Scale</h3>
                    <p><strong>transform: scale(x, y)</strong>: Resize element.</p>
                    <p>scale(1.5): 150% size. scale(0.5): 50% size.</p>
                """,
                "task": "Scale an element to 1.5 times its size.",
                "hint": "div { transform: scale(1.5); }",
                "starter_code": "<style>\n  div {\n    width: 100px;\n    height: 100px;\n    background: green;\n    /* Add scale */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["transform:", "scale"]
            },
            
            # Level 13: Transforms - Skew
            {
                "id": "css_skew",
                "title": "Level 13: Transforms - Skew",
                "description": "Slant elements.",
                "content": """
                    <h3>Transform: Skew</h3>
                    <p><strong>transform: skew(x, y)</strong>: Slant element.</p>
                    <p><strong>skewX()</strong>: Horizontal skew.</p>
                    <p><strong>skewY()</strong>: Vertical skew.</p>
                """,
                "task": "Skew an element by 20 degrees on the X axis.",
                "hint": "div { transform: skewX(20deg); }",
                "starter_code": "<style>\n  div {\n    width: 100px;\n    height: 100px;\n    background: orange;\n    /* Add skew */\n  }\n</style>\n<div></div>",
                "validation_keywords": ["transform:", "skew"]
            },
            
            # Level 14: Position Part 1
            {
                "id": "css_position_1",
                "title": "Level 14: Position (Part 1)",
                "description": "Static, relative, and absolute positioning.",
                "content": """
                    <h3>Position Property</h3>
                    <p><strong>static</strong>: Default, normal flow.</p>
                    <p><strong>relative</strong>: Positioned relative to normal position.</p>
                    <p><strong>absolute</strong>: Positioned relative to nearest positioned ancestor.</p>
                """,
                "task": "Position an element absolutely within a relative container.",
                "hint": ".container { position: relative; } .box { position: absolute; top: 10px; }",
                "starter_code": "<style>\n  .container {\n    /* Position container */\n  }\n  .box {\n    /* Position box */\n  }\n</style>\n<div class='container'><div class='box'>Box</div></div>",
                "validation_keywords": ["position:", "relative", "absolute"]
            },
            
            # Level 15: Position Part 2
            {
                "id": "css_position_2",
                "title": "Level 15: Position (Part 2)",
                "description": "Fixed and sticky positioning.",
                "content": """
                    <h3>Advanced Positioning</h3>
                    <p><strong>fixed</strong>: Fixed relative to viewport (stays on scroll).</p>
                    <p><strong>sticky</strong>: Toggles between relative and fixed.</p>
                    <p>Use with: top, right, bottom, left properties.</p>
                """,
                "task": "Create a fixed header that stays at the top.",
                "hint": "header { position: fixed; top: 0; width: 100%; }",
                "starter_code": "<style>\n  header {\n    /* Fix to top */\n  }\n</style>\n<header>Header</header>",
                "validation_keywords": ["position:", "fixed", "top:"]
            },
            
            # Level 16: Transitions
            {
                "id": "css_transitions",
                "title": "Level 16: Transitions",
                "description": "Smooth property changes.",
                "content": """
                    <h3>CSS Transitions</h3>
                    <p><strong>transition</strong>: property duration timing-function.</p>
                    <p>Example: transition: all 0.3s ease;</p>
                    <p>Commonly used with :hover pseudo-class.</p>
                """,
                "task": "Add a smooth transition to a hover effect.",
                "hint": "button { transition: all 0.3s; } button:hover { background: blue; }",
                "starter_code": "<style>\n  button {\n    /* Add transition */\n  }\n  button:hover {\n    background: blue;\n  }\n</style>\n<button>Hover me</button>",
                "validation_keywords": ["transition:", ":hover"]
            },
            
            # Level 17: Display Part 1
            {
                "id": "css_display_1",
                "title": "Level 17: Display (Part 1)",
                "description": "Block and inline elements.",
                "content": """
                    <h3>Display Property</h3>
                    <p><strong>display: block</strong>: Takes full width, starts on new line.</p>
                    <p><strong>display: inline</strong>: Takes only needed width, stays in line.</p>
                    <p>Block elements: div, p, h1. Inline elements: span, a, strong.</p>
                """,
                "task": "Change a span to display as block and a div to display as inline.",
                "hint": "span { display: block; } div { display: inline; }",
                "starter_code": "<style>\n  span {\n    /* Make block */\n  }\n  div {\n    /* Make inline */\n  }\n</style>\n<span>Span</span><div>Div</div>",
                "validation_keywords": ["display:", "block", "inline"]
            },
            
            # Level 18: Display Part 2
            {
                "id": "css_display_2",
                "title": "Level 18: Display (Part 2)",
                "description": "Inline-block and hiding elements.",
                "content": """
                    <h3>More Display Values</h3>
                    <p><strong>display: inline-block</strong>: Inline but can have width/height.</p>
                    <p><strong>display: none</strong>: Completely hides element.</p>
                    <p>Inline-block is useful for creating horizontal layouts.</p>
                """,
                "task": "Create inline-block elements and hide an element with display none.",
                "hint": ".box { display: inline-block; } .hidden { display: none; }",
                "starter_code": "<style>\n  .box {\n    width: 100px;\n    height: 100px;\n    background: red;\n    /* Make inline-block */\n  }\n  .hidden {\n    /* Hide element */\n  }\n</style>\n<div class='box'>1</div><div class='box'>2</div><div class='hidden'>Hidden</div>",
                "validation_keywords": ["display:", "inline-block", "none"]
            }
        ]
    },
    
    "js": {
        "title": "Module 3: The Brain (JavaScript)",
        "description": "Inject logic. Animate the construct and handle interactions.",
        "missions": [
            # Output Methods
            {
                "id": "js_alert",
                "title": "Level 1: Alert",
                "description": "Display popup messages.",
                "content": """
                    <h3>Alert</h3>
                    <p><strong>alert('message')</strong>: Shows a popup message box.</p>
                """,
                "task": "Create an alert with the message 'Hello World'.",
                "hint": "alert('Hello World');",
                "starter_code": "<script>\n  // Add alert\n</script>",
                "validation_keywords": ["alert", "Hello"]
            },
            {
                "id": "js_console",
                "title": "Level 2: Console Log",
                "description": "Log to the developer console.",
                "content": """
                    <h3>Console Log</h3>
                    <p><strong>console.log('message')</strong>: Prints to the console.</p>
                """,
                "task": "Log 'System Ready' to the console.",
                "hint": "console.log('System Ready');",
                "starter_code": "<script>\n  // Log message\n</script>",
                "validation_keywords": ["console.log", "System Ready"]
            },
            
            # Variables
            {
                "id": "js_var",
                "title": "Level 3: Variables (var)",
                "description": "Store data with var.",
                "content": """
                    <h3>Variables</h3>
                    <p><strong>var name = value;</strong>: Declares a variable.</p>
                """,
                "task": "Declare a variable 'score' and set it to 100.",
                "hint": "var score = 100;",
                "starter_code": "<script>\n  // Declare variable\n</script>",
                "validation_keywords": ["var", "score", "=", "100"]
            },
            {
                "id": "js_let_const",
                "title": "Level 4: Let & Const",
                "description": "Modern variable declarations.",
                "content": """
                    <h3>Let & Const</h3>
                    <p><strong>let</strong>: Block-scoped variable (can change).</p>
                    <p><strong>const</strong>: Block-scoped constant (cannot change).</p>
                """,
                "task": "Declare a const 'PI' with value 3.14 and log it.",
                "hint": "const PI = 3.14; console.log(PI);",
                "starter_code": "<script>\n  // Use const\n</script>",
                "validation_keywords": ["const", "PI", "3.14", "console.log"]
            },
            
            # Data Types - Numbers
            {
                "id": "js_numbers",
                "title": "Level 5: Numbers",
                "description": "Work with numeric data.",
                "content": """
                    <h3>Numbers</h3>
                    <p>JavaScript numbers can be integers or decimals.</p>
                    <p>Example: var age = 25; var price = 19.99;</p>
                """,
                "task": "Create a variable 'age' with value 25 and log it.",
                "hint": "var age = 25; console.log(age);",
                "starter_code": "<script>\n  // Create number\n</script>",
                "validation_keywords": ["var", "age", "25", "console.log"]
            },
            {
                "id": "js_number_methods",
                "title": "Level 6: Number Methods",
                "description": "Convert and parse numbers.",
                "content": """
                    <h3>Number Methods</h3>
                    <p><strong>parseInt()</strong>: Convert string to integer.</p>
                    <p><strong>parseFloat()</strong>: Convert string to decimal.</p>
                """,
                "task": "Convert the string '42' to a number using parseInt and log it.",
                "hint": "var num = parseInt('42'); console.log(num);",
                "starter_code": "<script>\n  // Parse number\n</script>",
                "validation_keywords": ["parseInt", "42", "console.log"]
            },
            
            # Data Types - Strings
            {
                "id": "js_strings",
                "title": "Level 7: Strings",
                "description": "Work with text data.",
                "content": """
                    <h3>Strings</h3>
                    <p>Text enclosed in quotes: 'text' or "text"</p>
                    <p><strong>.length</strong>: Get string length.</p>
                """,
                "task": "Create a string 'hello' and log its length.",
                "hint": "var text = 'hello'; console.log(text.length);",
                "starter_code": "<script>\n  // String length\n</script>",
                "validation_keywords": ["var", "hello", "length", "console.log"]
            },
            {
                "id": "js_string_methods",
                "title": "Level 8: String Methods",
                "description": "Manipulate strings.",
                "content": """
                    <h3>String Methods</h3>
                    <p><strong>.toUpperCase()</strong>: Convert to uppercase.</p>
                    <p><strong>.toLowerCase()</strong>: Convert to lowercase.</p>
                """,
                "task": "Create a string 'hello' and convert it to uppercase.",
                "hint": "var text = 'hello'; console.log(text.toUpperCase());",
                "starter_code": "<script>\n  // String operations\n</script>",
                "validation_keywords": ["var", "hello", "toUpperCase()"]
            },
            
            # Operators
            {
                "id": "js_arithmetic",
                "title": "Level 9: Arithmetic",
                "description": "Basic math operations.",
                "content": """
                    <h3>Arithmetic Operators</h3>
                    <p><strong>+</strong>: Addition</p>
                    <p><strong>-</strong>: Subtraction</p>
                    <p><strong>*</strong>: Multiplication</p>
                    <p><strong>/</strong>: Division</p>
                """,
                "task": "Calculate 10 + 5 and log the result.",
                "hint": "console.log(10 + 5);",
                "starter_code": "<script>\n  // Calculate\n</script>",
                "validation_keywords": ["console.log", "10", "+", "5"]
            },
            {
                "id": "js_increment",
                "title": "Level 10: Increment/Decrement",
                "description": "Increase or decrease values.",
                "content": """
                    <h3>Increment & Decrement</h3>
                    <p><strong>++</strong>: Increment by 1</p>
                    <p><strong>--</strong>: Decrement by 1</p>
                """,
                "task": "Create a variable 'count' = 5, increment it, and log it.",
                "hint": "var count = 5; count++; console.log(count);",
                "starter_code": "<script>\n  // Increment\n</script>",
                "validation_keywords": ["var", "count", "++", "console.log"]
            },
            
            # Conditionals
            {
                "id": "js_comparison",
                "title": "Level 11: Comparison",
                "description": "Compare values.",
                "content": """
                    <h3>Comparison Operators</h3>
                    <p><strong>></strong>: Greater than</p>
                    <p><strong><</strong>: Less than</p>
                    <p><strong>===</strong>: Equal to</p>
                    <p><strong>!==</strong>: Not equal to</p>
                """,
                "task": "Log the result of 5 > 2.",
                "hint": "console.log(5 > 2);",
                "starter_code": "<script>\n  // Compare\n</script>",
                "validation_keywords": ["console.log", "5", ">", "2"]
            },
            {
                "id": "js_if",
                "title": "Level 12: If Statements",
                "description": "Make decisions.",
                "content": """
                    <h3>If Statement</h3>
                    <p><strong>if (condition) { ... }</strong>: Execute if true.</p>
                """,
                "task": "Check if 5 > 2, if so alert 'True'.",
                "hint": "if (5 > 2) { alert('True'); }",
                "starter_code": "<script>\n  // Add condition\n</script>",
                "validation_keywords": ["if", "5", ">", "2", "alert", "True"]
            },
            {
                "id": "js_else",
                "title": "Level 13: Else Statements",
                "description": "Handle alternatives.",
                "content": """
                    <h3>Else</h3>
                    <p><strong>else { ... }</strong>: Executes when if is false.</p>
                """,
                "task": "Check if 3 > 5, alert 'Yes' if true, else alert 'No'.",
                "hint": "if (3 > 5) { alert('Yes'); } else { alert('No'); }",
                "starter_code": "<script>\n  // If-else\n</script>",
                "validation_keywords": ["if", "else", "alert"]
            },
            
            # Arrays
            {
                "id": "js_arrays_create",
                "title": "Level 14: Creating Arrays",
                "description": "Store multiple values.",
                "content": """
                    <h3>Arrays</h3>
                    <p><strong>var arr = [1, 2, 3];</strong>: Creates an array.</p>
                """,
                "task": "Create an array with 3 numbers and log it.",
                "hint": "var numbers = [1, 2, 3]; console.log(numbers);",
                "starter_code": "<script>\n  // Create array\n</script>",
                "validation_keywords": ["var", "[", "]", "console.log"]
            },
            {
                "id": "js_arrays_access",
                "title": "Level 15: Accessing Arrays",
                "description": "Get array elements.",
                "content": """
                    <h3>Array Access</h3>
                    <p><strong>arr[0]</strong>: Access first element (index 0).</p>
                    <p><strong>.length</strong>: Get array size.</p>
                """,
                "task": "Create array [10, 20, 30], log the first element.",
                "hint": "var nums = [10, 20, 30]; console.log(nums[0]);",
                "starter_code": "<script>\n  // Access array\n</script>",
                "validation_keywords": ["var", "[", "]", "[0]", "console.log"]
            },
            
            # Loops
            {
                "id": "js_for_loop",
                "title": "Level 16: For Loops",
                "description": "Repeat code.",
                "content": """
                    <h3>For Loop</h3>
                    <p><strong>for (var i = 0; i < 5; i++) { ... }</strong></p>
                    <p>Repeats code a specific number of times.</p>
                """,
                "task": "Create a for loop that logs numbers 0 to 4.",
                "hint": "for (var i = 0; i < 5; i++) { console.log(i); }",
                "starter_code": "<script>\n  // For loop\n</script>",
                "validation_keywords": ["for", "var", "i", "<", "console.log"]
            },
            {
                "id": "js_while_loop",
                "title": "Level 17: While Loops",
                "description": "Loop with condition.",
                "content": """
                    <h3>While Loop</h3>
                    <p><strong>while (condition) { ... }</strong></p>
                    <p>Repeats while condition is true.</p>
                """,
                "task": "Create a variable 'i' = 0, while i < 3, log i and increment.",
                "hint": "var i = 0; while (i < 3) { console.log(i); i++; }",
                "starter_code": "<script>\n  // While loop\n</script>",
                "validation_keywords": ["var", "while", "<", "console.log", "++"]
            },
            
            # Functions
            {
                "id": "js_functions_basic",
                "title": "Level 18: Functions",
                "description": "Reusable code blocks.",
                "content": """
                    <h3>Functions</h3>
                    <p><strong>function name() { ... }</strong>: Defines a function.</p>
                    <p>Call with: <strong>name();</strong></p>
                """,
                "task": "Create a function 'greet' that alerts 'Hi'.",
                "hint": "function greet() { alert('Hi'); }",
                "starter_code": "<script>\n  // Define function\n</script>",
                "validation_keywords": ["function", "greet", "alert", "Hi"]
            },
            {
                "id": "js_functions_params",
                "title": "Level 19: Function Parameters",
                "description": "Pass data to functions.",
                "content": """
                    <h3>Parameters</h3>
                    <p><strong>function greet(name) { ... }</strong></p>
                    <p>Parameters let you pass values to functions.</p>
                """,
                "task": "Create function 'sayHello' with parameter 'name', alert 'Hello ' + name.",
                "hint": "function sayHello(name) { alert('Hello ' + name); }",
                "starter_code": "<script>\n  // Function with parameter\n</script>",
                "validation_keywords": ["function", "sayHello", "name", "alert", "Hello"]
            },
            {
                "id": "js_functions_return",
                "title": "Level 20: Return Values",
                "description": "Get results from functions.",
                "content": """
                    <h3>Return</h3>
                    <p><strong>return value;</strong>: Sends a value back.</p>
                """,
                "task": "Create function 'add' that takes two numbers and returns their sum.",
                "hint": "function add(a, b) { return a + b; }",
                "starter_code": "<script>\n  // Function with return\n</script>",
                "validation_keywords": ["function", "add", "return", "+"]
            },
            
            # DOM Manipulation
            {
                "id": "js_getelementbyid",
                "title": "Level 21: Get Element by ID",
                "description": "Select HTML elements.",
                "content": """
                    <h3>DOM Selection</h3>
                    <p><strong>document.getElementById('id')</strong>: Finds element by ID.</p>
                """,
                "task": "Select the element with id 'demo'.",
                "hint": "document.getElementById('demo')",
                "starter_code": "<div id='demo'>Text</div>\n<script>\n  // Select element\n</script>",
                "validation_keywords": ["document.getElementById", "demo"]
            },
            {
                "id": "js_innerhtml",
                "title": "Level 22: Change Content",
                "description": "Modify HTML content.",
                "content": """
                    <h3>innerHTML</h3>
                    <p><strong>element.innerHTML = 'text'</strong>: Changes content.</p>
                """,
                "task": "Change element with id 'msg' to 'Updated'.",
                "hint": "document.getElementById('msg').innerHTML = 'Updated';",
                "starter_code": "<div id='msg'>Old</div>\n<script>\n  // Update content\n</script>",
                "validation_keywords": ["getElementById", "msg", "innerHTML", "Updated"]
            },
            {
                "id": "js_innertext",
                "title": "Level 23: Change Text",
                "description": "Modify text content.",
                "content": """
                    <h3>innerText</h3>
                    <p><strong>element.innerText = 'text'</strong>: Changes text only.</p>
                    <p>Unlike innerHTML, this doesn't interpret HTML tags.</p>
                """,
                "task": "Change the text of element with id 'txt' to 'New Text'.",
                "hint": "document.getElementById('txt').innerText = 'New Text';",
                "starter_code": "<div id='txt'>Old</div>\n<script>\n  // Change text\n</script>",
                "validation_keywords": ["getElementById", "txt", "innerText", "New Text"]
            },
            {
                "id": "js_style_color",
                "title": "Level 24: Change Color",
                "description": "Modify element color.",
                "content": """
                    <h3>Style - Color</h3>
                    <p><strong>element.style.color = 'red'</strong>: Changes text color.</p>
                """,
                "task": "Change the color of element with id 'box' to red.",
                "hint": "document.getElementById('box').style.color = 'red';",
                "starter_code": "<div id='box'>Text</div>\n<script>\n  // Change color\n</script>",
                "validation_keywords": ["getElementById", "box", "style", "color", "red"]
            },
            {
                "id": "js_style_background",
                "title": "Level 25: Change Background",
                "description": "Modify background color.",
                "content": """
                    <h3>Style - Background</h3>
                    <p><strong>element.style.backgroundColor = 'blue'</strong></p>
                """,
                "task": "Change background of element with id 'div1' to blue.",
                "hint": "document.getElementById('div1').style.backgroundColor = 'blue';",
                "starter_code": "<div id='div1'>Box</div>\n<script>\n  // Change background\n</script>",
                "validation_keywords": ["getElementById", "div1", "style", "backgroundColor", "blue"]
            },
            
            # Events
            {
                "id": "js_onclick",
                "title": "Level 26: Click Events",
                "description": "Respond to clicks.",
                "content": """
                    <h3>Onclick</h3>
                    <p><strong>onclick='code'</strong>: Runs when clicked.</p>
                """,
                "task": "Create a button that alerts 'Clicked!' when clicked.",
                "hint": "<button onclick='alert(\"Clicked!\")'>Click</button>",
                "starter_code": "<!-- Create button -->\n",
                "validation_keywords": ["<button", "onclick=", "alert", "Clicked"]
            },
            {
                "id": "js_onmouseover",
                "title": "Level 27: Mouse Over",
                "description": "Respond to hover.",
                "content": """
                    <h3>Onmouseover</h3>
                    <p><strong>onmouseover</strong>: When mouse enters element.</p>
                """,
                "task": "Create a div that changes background to blue on mouseover.",
                "hint": "<div onmouseover='this.style.background=\"blue\"'>Hover</div>",
                "starter_code": "<!-- Create interactive div -->\n",
                "validation_keywords": ["onmouseover", "style", "background"]
            },
            {
                "id": "js_onmouseout",
                "title": "Level 28: Mouse Out",
                "description": "Respond to mouse leaving.",
                "content": """
                    <h3>Onmouseout</h3>
                    <p><strong>onmouseout</strong>: When mouse leaves element.</p>
                """,
                "task": "Create a div that changes to red on mouseover and white on mouseout.",
                "hint": "<div onmouseover='this.style.background=\"red\"' onmouseout='this.style.background=\"white\"'>Hover</div>",
                "starter_code": "<!-- Create div -->\n",
                "validation_keywords": ["onmouseover", "onmouseout", "style", "background"]
            }
        ]
    },
    
    "challenges": {
        "title": "Module 4: The Trials (Challenges)",
        "description": "Test your skills through progressive challenges from easy to hard.",
        "missions": [
            # EASY CHALLENGES (1-5)
            {
                "id": "challenge_01",
                "title": "Challenge 1: Profile Card [EASY]",
                "description": "Create a basic profile card.",
                "content": """
                    <h3>Challenge: Profile Card</h3>
                    <p><strong>Concepts</strong>: HTML structure, semantic tags</p>
                """,
                "task": "Create a profile card with header (h1 name), main (img, h2 title, p bio), and footer.",
                "hint": "Use <header>, <main>, <footer> tags.",
                "starter_code": "<!-- Build profile card -->\n",
                "validation_keywords": ["<header", "<h1", "<main>", "<img", "alt=", "<h2", "<p", "<footer"]
            },
            {
                "id": "challenge_02",
                "title": "Challenge 2: Colorful Menu [EASY]",
                "description": "Style a navigation menu.",
                "content": """
                    <h3>Challenge: Colorful Menu</h3>
                    <p><strong>Concepts</strong>: CSS selectors, colors, lists</p>
                """,
                "task": "Style nav list: remove bullets, white text, dark background, 18px, uppercase.",
                "hint": "Use list-style-type, color, background, font-size, text-transform",
                "starter_code": "<style>\n  /* Add styles */\n</style>\n<nav><ul><li>Home</li><li>About</li></ul></nav>",
                "validation_keywords": ["list-style-type:", "none", "color:", "white", "background", "font-size:", "18px", "text-transform:", "uppercase"]
            },
            {
                "id": "challenge_03",
                "title": "Challenge 3: Hover Magic [EASY]",
                "description": "Add hover effects.",
                "content": """
                    <h3>Challenge: Hover Magic</h3>
                    <p><strong>Concepts</strong>: Transitions, transforms, hover</p>
                """,
                "task": "Add 0.3s transition, on hover: scale 1.1 and blue background.",
                "hint": "transition: all 0.3s; button:hover { transform: scale(1.1); }",
                "starter_code": "<style>\n  /* Add styles */\n</style>\n<button>Hover Me</button>",
                "validation_keywords": ["transition:", "0.3s", ":hover", "transform:", "scale", "1.1", "background"]
            },
            {
                "id": "challenge_04",
                "title": "Challenge 4: Alert Master [EASY]",
                "description": "Interactive alert button.",
                "content": """
                    <h3>Challenge: Alert Master</h3>
                    <p><strong>Concepts</strong>: Variables, alert, onclick</p>
                """,
                "task": "Create variable 'message' = 'Welcome!', button that alerts it.",
                "hint": "var message = 'Welcome!'; onclick='alert(message)'",
                "starter_code": "<script>\n  // Code here\n</script>",
                "validation_keywords": ["var", "message", "=", "Welcome", "button", "onclick=", "alert(message)"]
            },
            {
                "id": "challenge_05",
                "title": "Challenge 5: Text Transformer [EASY]",
                "description": "String manipulation.",
                "content": """
                    <h3>Challenge: Text Transformer</h3>
                    <p><strong>Concepts</strong>: Strings, methods</p>
                """,
                "task": "Variable 'text' = 'hello world', convert to uppercase, log it.",
                "hint": "var text = 'hello world'; console.log(text.toUpperCase());",
                "starter_code": "<script>\n  // Transform text\n</script>",
                "validation_keywords": ["var", "text", "hello world", "toUpperCase()", "console.log"]
            },
            
            # MEDIUM CHALLENGES (6-12)
            {
                "id": "challenge_06",
                "title": "Challenge 6: Navigation Bar [MEDIUM]",
                "description": "Complete horizontal nav bar.",
                "content": """
                    <h3>Challenge: Navigation Bar</h3>
                    <p><strong>Concepts</strong>: HTML nav, CSS display, flexbox, hover</p>
                """,
                "task": "Build nav with ul, 4 links. Style: horizontal, dark background, white text, padding, hover effect.",
                "hint": "Use display: flex or inline-block",
                "starter_code": "<!-- Create nav -->\n<style>\n  /* Styles */\n</style>",
                "validation_keywords": ["<nav", "<ul", "<li", "<a", "display:", "background", "padding:", ":hover"]
            },
            {
                "id": "challenge_07",
                "title": "Challenge 7: Image Gallery [MEDIUM]",
                "description": "Responsive image grid.",
                "content": """
                    <h3>Challenge: Image Gallery</h3>
                    <p><strong>Concepts</strong>: CSS grid, box model</p>
                """,
                "task": "Create div.gallery with 6 img tags. Style with grid, 3 columns, gap, borders.",
                "hint": "display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;",
                "starter_code": "<!-- Gallery -->\n<style>\n  /* Styles */\n</style>",
                "validation_keywords": ["<div", "class=", "gallery", "<img", "display:", "grid", "grid-template-columns:", "gap:", "border:"]
            },
            {
                "id": "challenge_08",
                "title": "Challenge 8: Form Validator [MEDIUM]",
                "description": "Validate form input.",
                "content": """
                    <h3>Challenge: Form Validator</h3>
                    <p><strong>Concepts</strong>: Forms, JS validation, DOM</p>
                """,
                "task": "Form with name input and button. Check if empty, alert 'Please enter name'.",
                "hint": "getElementById() and check if value === ''",
                "starter_code": "<form>\n  <!-- Form -->\n</form>\n<script>\n  // Validation\n</script>",
                "validation_keywords": ["<form", "<input", "type=", "text", "<button", "getElementById", "if", "===", "alert"]
            },
            {
                "id": "challenge_09",
                "title": "Challenge 9: Counter App [MEDIUM]",
                "description": "Click counter.",
                "content": """
                    <h3>Challenge: Counter App</h3>
                    <p><strong>Concepts</strong>: Variables, DOM, events, operators</p>
                """,
                "task": "Counter display and +/- buttons. Clicking changes count, update display.",
                "hint": "var count = 0; getElementById(); innerHTML; ++/--",
                "starter_code": "<div id='display'>0</div>\n<!-- Buttons -->\n<script>\n  // Counter logic\n</script>",
                "validation_keywords": ["var", "count", "getElementById", "innerHTML", "++", "--", "onclick="]
            },
            {
                "id": "challenge_10",
                "title": "Challenge 10: Animated Box [MEDIUM]",
                "description": "CSS keyframe animation.",
                "content": """
                    <h3>Challenge: Animated Box</h3>
                    <p><strong>Concepts</strong>: Animations, @keyframes, transforms</p>
                """,
                "task": "100x100px box. @keyframes 'spin' rotates 360deg. Apply animation: spin 2s infinite.",
                "hint": "@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }",
                "starter_code": "<style>\n  .box { width: 100px; height: 100px; background: red; }\n  /* Animation */\n</style>\n<div class='box'></div>",
                "validation_keywords": ["@keyframes", "spin", "transform:", "rotate", "360deg", "animation:", "2s", "infinite"]
            },
            {
                "id": "challenge_11",
                "title": "Challenge 11: Todo Item [MEDIUM]",
                "description": "Single todo item.",
                "content": """
                    <h3>Challenge: Todo Item</h3>
                    <p><strong>Concepts</strong>: Forms, flexbox, styling</p>
                """,
                "task": "div.todo with checkbox, label, delete button. Style with flexbox, padding, border, hover.",
                "hint": "display: flex; justify-content: space-between;",
                "starter_code": "<!-- Todo item -->\n<style>\n  /* Styles */\n</style>",
                "validation_keywords": ["<div", "class=", "todo", "<input", "type=", "checkbox", "<label", "<button", "display:", "flex", "padding:", "border:"]
            },
            {
                "id": "challenge_12",
                "title": "Challenge 12: Color Picker [MEDIUM]",
                "description": "Change background color.",
                "content": """
                    <h3>Challenge: Color Picker</h3>
                    <p><strong>Concepts</strong>: DOM styling, events</p>
                """,
                "task": "3 buttons (Red, Blue, Green). Clicking changes document.body.style.backgroundColor.",
                "hint": "onclick='document.body.style.backgroundColor = \"red\"'",
                "starter_code": "<!-- Color buttons -->\n<script>\n  // Logic\n</script>",
                "validation_keywords": ["<button", "onclick=", "document.body.style.backgroundColor", "red", "blue", "green"]
            },
            
            # HARD CHALLENGES (13-20)
            {
                "id": "challenge_13",
                "title": "Challenge 13: Landing Page [HARD]",
                "description": "Complete landing page.",
                "content": """
                    <h3>Challenge: Landing Page</h3>
                    <p><strong>Concepts</strong>: Full HTML structure, advanced CSS</p>
                """,
                "task": "Build page: header (nav+logo), hero (h1+p+button), features (3 divs), footer. Fully styled.",
                "hint": "Use semantic HTML, flexbox/grid, consistent colors",
                "starter_code": "<!-- Landing page -->\n<style>\n  /* All styles */\n</style>",
                "validation_keywords": ["<header", "<nav", "<section", "<h1", "<button", "<footer", "display:", "flex", "grid", "padding:", "margin:"]
            },
            {
                "id": "challenge_14",
                "title": "Challenge 14: Calculator [HARD]",
                "description": "Functional calculator.",
                "content": """
                    <h3>Challenge: Calculator</h3>
                    <p><strong>Concepts</strong>: Complex JS logic, operators, DOM</p>
                """,
                "task": "Calculator with display, buttons (0-9, +, -, *, /, =, C). Implement calculation logic.",
                "hint": "Use eval() or switch/if statements",
                "starter_code": "<div id='display'>0</div>\n<!-- Buttons -->\n<script>\n  // Calculator\n</script>",
                "validation_keywords": ["<div", "id=", "display", "<button", "onclick=", "function", "if", "+", "-", "*", "/"]
            },
            {
                "id": "challenge_15",
                "title": "Challenge 15: Image Slider [HARD]",
                "description": "Image carousel.",
                "content": """
                    <h3>Challenge: Image Slider</h3>
                    <p><strong>Concepts</strong>: Advanced DOM, arrays, positioning</p>
                """,
                "task": "Slider with 3+ images, prev/next buttons. Show one image at a time, buttons cycle through.",
                "hint": "Array of URLs, currentIndex variable, update src on click",
                "starter_code": "<div class='slider'>\n  <button id='prev'>←</button>\n  <img id='slideImg' src='' alt='Slide'>\n  <button id='next'>→</button>\n</div>\n<script>\n  var images = ['url1', 'url2', 'url3'];\n  // Slider logic\n</script>",
                "validation_keywords": ["var", "images", "currentIndex", "getElementById", "onclick=", "if", "src", "++", "--"]
            },
            {
                "id": "challenge_16",
                "title": "Challenge 16: Quiz App [HARD]",
                "description": "Multiple-choice quiz.",
                "content": """
                    <h3>Challenge: Quiz App</h3>
                    <p><strong>Concepts</strong>: State management, arrays, objects, logic</p>
                """,
                "task": "Quiz with 3 questions, radio buttons, submit button. Check answers, display score.",
                "hint": "Store correct answers in array, compare with selections",
                "starter_code": "<div id='quiz'>\n  <!-- Questions -->\n</div>\n<button onclick='checkAnswers()'>Submit</button>\n<div id='result'></div>\n<script>\n  var correctAnswers = ['a', 'b', 'c'];\n  // Quiz logic\n</script>",
                "validation_keywords": ["<input", "type=", "radio", "name=", "function", "getElementById", "if", "===", "innerHTML"]
            },
            {
                "id": "challenge_17",
                "title": "Challenge 17: Todo List [HARD]",
                "description": "Full todo list app.",
                "content": """
                    <h3>Challenge: Todo List</h3>
                    <p><strong>Concepts</strong>: CRUD operations, DOM manipulation, arrays</p>
                """,
                "task": "Input + add button. Display todos in list. Each has checkbox (toggle) and delete button. Store in array.",
                "hint": "Array to store, createElement() to add, remove() to delete",
                "starter_code": "<input type='text' id='todoInput' placeholder='New todo'>\n<button onclick='addTodo()'>Add</button>\n<ul id='todoList'></ul>\n<script>\n  var todos = [];\n  // Functions\n</script>",
                "validation_keywords": ["var", "todos", "function", "getElementById", "value", "createElement", "appendChild", "remove", "onclick="]
            },
            {
                "id": "challenge_18",
                "title": "Challenge 18: Weather Card [HARD]",
                "description": "Beautiful weather display.",
                "content": """
                    <h3>Challenge: Weather Card</h3>
                    <p><strong>Concepts</strong>: Advanced CSS, gradients, shadows, JS data</p>
                """,
                "task": "Weather card: city, temperature, condition, icon. Use gradients, shadows. Update with JS.",
                "hint": "linear-gradient, box-shadow, border-radius, innerHTML",
                "starter_code": "<div class='weather-card'>\n  <h2 id='city'>City</h2>\n  <div id='temp'>--°</div>\n  <p id='condition'>--</p>\n</div>\n<style>\n  /* Beautiful styles */\n</style>\n<script>\n  // Update data\n</script>",
                "validation_keywords": ["class=", "weather-card", "gradient", "box-shadow", "border-radius", "getElementById", "innerHTML"]
            },
            {
                "id": "challenge_19",
                "title": "Challenge 19: Interactive Dashboard [HARD]",
                "description": "Dashboard with components.",
                "content": """
                    <h3>Challenge: Interactive Dashboard</h3>
                    <p><strong>Concepts</strong>: Complex layout, multiple components, state</p>
                """,
                "task": "Dashboard: header, sidebar (nav), main (3 stat cards, chart div), footer. Interactive stats.",
                "hint": "CSS Grid for layout, flexbox for components, JS to update numbers",
                "starter_code": "<!-- Dashboard -->\n<style>\n  /* Dashboard styles */\n</style>\n<script>\n  // Interactivity\n</script>",
                "validation_keywords": ["<header", "<aside", "<main", "<section", "display:", "grid", "flex", "getElementById", "innerHTML", "onclick="]
            },
            {
                "id": "challenge_20",
                "title": "Challenge 20: Mini Portfolio [HARD]",
                "description": "Complete portfolio website.",
                "content": """
                    <h3>Challenge: Mini Portfolio</h3>
                    <p><strong>Concepts</strong>: Everything! Full HTML/CSS/JS integration</p>
                """,
                "task": "Portfolio: nav (smooth scroll), hero, about, projects grid (3 cards), contact form, footer. Fully styled and interactive.",
                "hint": "Use all learned concepts: semantic HTML, flexbox/grid, animations, form validation, DOM manipulation",
                "starter_code": "<!-- Complete portfolio -->\n<style>\n  /* All styles */\n</style>\n<script>\n  // All interactivity\n</script>",
                "validation_keywords": ["<header", "<nav", "<section", "<article", "<form", "<footer", "display:", "grid", "flex", "transition:", "animation:", "getElementById", "function"]
            }
        ]
    }
}


