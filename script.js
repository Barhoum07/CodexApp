document.addEventListener('DOMContentLoaded', () => {
    const runBtn = document.getElementById('run-btn');
    const htmlEditor = document.getElementById('html-editor');
    const cssEditor = document.getElementById('css-editor');
    const jsEditor = document.getElementById('js-editor');
    const preview = document.getElementById('preview-frame');
    const missionId = document.getElementById('mission-id');

    // Tab buttons
    const tabBtns = document.querySelectorAll('.tab-btn');
    const editors = document.querySelectorAll('.code-editor');

    // Modal elements
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalMessage = document.getElementById('modal-message');
    const modalClose = document.getElementById('modal-close');
    const nextMissionBtn = document.getElementById('next-mission-btn');
    const homeBtn = document.getElementById('home-btn');

    // Initialize CodeMirror editors with enhanced autocomplete
    let cmHtml, cmCss, cmJs;

    // Common HTML tags for custom autocomplete
    const commonHtmlTags = [
        "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr"
    ];

    function customHtmlHint(cm, options) {
        const cur = cm.getCursor();
        const token = cm.getTokenAt(cur);
        const inner = CodeMirror.innerMode(cm.getMode(), token.state).state;

        // 1. If we are inside a tag (attributes) or typing a tag name after <
        // Use standard hint for these cases as it handles them well
        if (inner.tagName || token.type === "tag" || token.string.startsWith("<")) {
            return CodeMirror.hint.html(cm, options);
        }

        // 2. Custom logic: If typing a word in text content
        if (token.type === null || token.type === "text" || token.type === "variable") {
            const word = token.string.trim();
            let list = [];

            // Emmet suggestions
            if (window.emmet) {
                const line = cm.getLine(cur.line);
                const before = line.slice(0, cur.ch);
                // Include ! in the regex
                const match = before.match(/[\w:>+.*#$-{}[\]()!]+$/);
                if (match) {
                    const abbr = match[0];
                    try {
                        const expanded = emmet.expandAbbreviation(abbr, { syntax: 'html' });
                        if (expanded && expanded !== abbr) {
                            list.push({
                                text: expanded,
                                displayText: abbr + ' (Emmet)',
                                hint: function (cm, self, data) {
                                    // Calculate start position based on abbreviation length
                                    const from = CodeMirror.Pos(cur.line, cur.ch - abbr.length);
                                    cm.replaceRange(data.text, from, cur);
                                }
                            });
                        }
                    } catch (e) { }
                }
            }

            if (word.match(/^[a-zA-Z]+$/)) {
                const simpleTags = commonHtmlTags.filter(t => t.startsWith(word.toLowerCase())).map(t => {
                    return {
                        text: "<" + t,
                        displayText: t,
                        hint: function (cm, self, data) {
                            cm.replaceRange(data.text, self.from, self.to);
                            // Trigger autocomplete again to show attributes or close tag
                            setTimeout(() => {
                                CodeMirror.commands.autocomplete(cm);
                            }, 100);
                        }
                    };
                });
                list = list.concat(simpleTags);
            }

            if (list.length > 0) {
                return {
                    list: list,
                    from: CodeMirror.Pos(cur.line, token.start),
                    to: CodeMirror.Pos(cur.line, token.end)
                };
            }
        }

        // 3. Fallback to standard hint
        return CodeMirror.hint.html(cm, options);
    }

    if (htmlEditor) {
        cmHtml = CodeMirror.fromTextArea(htmlEditor, {
            lineNumbers: true,
            mode: 'htmlmixed',
            theme: 'monokai',
            lineWrapping: true,
            matchBrackets: true,
            styleActiveLine: true,
            highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: true },
            matchTags: { bothTags: true },
            foldGutter: true,
            gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"],
            extraKeys: {
                // Autocomplete
                "Ctrl-Space": "autocomplete",

                // VS Code: Line Manipulation
                "Alt-Up": "swapLineUp",
                "Alt-Down": "swapLineDown",
                "Shift-Alt-Up": function (cm) {
                    // Duplicate line up
                    const cursor = cm.getCursor();
                    const line = cm.getLine(cursor.line);
                    cm.replaceRange(line + "\n", { line: cursor.line, ch: 0 });
                },
                "Shift-Alt-Down": function (cm) {
                    // Duplicate line down
                    const cursor = cm.getCursor();
                    const line = cm.getLine(cursor.line);
                    cm.replaceRange("\n" + line, { line: cursor.line + 1, ch: 0 });
                },
                "Ctrl-Shift-K": "deleteLine",
                "Ctrl-Enter": function (cm) {
                    const cursor = cm.getCursor();
                    cm.replaceRange("\n", { line: cursor.line + 1, ch: 0 });
                    cm.setCursor({ line: cursor.line + 1, ch: 0 });
                },
                "Ctrl-Shift-Enter": function (cm) {
                    const cursor = cm.getCursor();
                    cm.replaceRange("\n", { line: cursor.line, ch: 0 });
                    cm.setCursor({ line: cursor.line, ch: 0 });
                },

                // VS Code: Indentation
                "Ctrl-]": "indentMore",
                "Ctrl-[": "indentLess",

                // VS Code: Comments
                "Ctrl-/": "toggleComment",
                "Shift-Alt-A": function (cm) {
                    cm.toggleComment({ blockComment: true });
                },

                // VS Code: Multi-cursor
                "Ctrl-D": function (cm) {
                    // Select next occurrence
                    if (cm.somethingSelected()) {
                        const selection = cm.getSelection();
                        const cursor = cm.getCursor("to");
                        const searchCursor = cm.getSearchCursor(selection, cursor);
                        if (searchCursor.findNext()) {
                            cm.addSelection(searchCursor.from(), searchCursor.to());
                        }
                    } else {
                        cm.execCommand("selectWordAt");
                    }
                },
                "Ctrl-Shift-L": function (cm) {
                    // Select all occurrences
                    if (cm.somethingSelected()) {
                        const selection = cm.getSelection();
                        const ranges = [];
                        const searchCursor = cm.getSearchCursor(selection);
                        while (searchCursor.findNext()) {
                            ranges.push({ anchor: searchCursor.from(), head: searchCursor.to() });
                        }
                        if (ranges.length > 0) {
                            cm.setSelections(ranges);
                        }
                    }
                },

                // VS Code: Search & Navigation
                "Ctrl-F": "find",
                "Ctrl-H": "replace",
                "F3": "findNext",
                "Shift-F3": "findPrev",
                "Ctrl-G": "jumpToLine",

                // HTML-specific: Tag manipulation
                "Alt-Shift-W": function (cm) {
                    // Wrap selection with tag
                    if (cm.somethingSelected()) {
                        const selection = cm.getSelection();
                        const tagName = prompt("Enter tag name:");
                        if (tagName) {
                            cm.replaceSelection(`<${tagName}>${selection}</${tagName}>`);
                        }
                    }
                    return CodeMirror.Pass;
                },

                // Emmet expansion on Tab (primary trigger)
                "Tab": function (cm) {
                    // First check if we should expand Emmet
                    if (window.emmet) {
                        var cur = cm.getCursor();
                        var line = cm.getLine(cur.line);
                        var before = line.slice(0, cur.ch);
                        // Enhanced regex to support {}, [], (), ! and other Emmet syntax
                        var match = before.match(/[\w:>+.*#$-{}[\]()!]+$/);
                        if (match) {
                            var abbr = match[0];
                            console.log("Emmet: Trying to expand abbreviation:", abbr);
                            try {
                                var expanded = emmet.expandAbbreviation(abbr, { syntax: 'html' });
                                console.log("Emmet: Expansion result:", expanded);
                                if (expanded && expanded !== abbr) {
                                    console.log("Emmet: Replacing with expanded code");
                                    cm.replaceRange(expanded, { line: cur.line, ch: cur.ch - abbr.length }, cur);
                                    // Don't return CodeMirror.Pass - expansion succeeded
                                    return;
                                }
                            } catch (e) {
                                console.log("Emmet: Expansion error:", e);
                                // If expansion fails, fall through to default Tab behavior
                            }
                        }
                    }
                    // Default tab behavior (indentation)
                    return CodeMirror.Pass;
                },

                // Emmet expansion on Enter (alternative trigger)
                "Enter": function (cm) {
                    if (window.emmet) {
                        var cur = cm.getCursor();
                        var line = cm.getLine(cur.line);
                        var before = line.slice(0, cur.ch).trim();

                        // Only expand on Enter for specific patterns to avoid annoying expansions
                        // Expand if it's a known Emmet abbreviation like "!", "html:5", etc.
                        if (before === '!' || before.match(/^(html|doc|css|js):/)) {
                            var match = before.match(/[\w:>+.*#$-{}[\]()!]+$/);
                            if (match) {
                                var abbr = match[0];
                                try {
                                    var expanded = emmet.expandAbbreviation(abbr, { syntax: 'html' });
                                    if (expanded && expanded !== abbr) {
                                        var startCh = cur.ch - abbr.length;
                                        cm.replaceRange(expanded, { line: cur.line, ch: startCh }, cur);
                                        return;
                                    }
                                } catch (e) {
                                    // Ignore
                                }
                            }
                        }
                    }
                    return CodeMirror.Pass;
                }
            },
            hintOptions: {
                hint: customHtmlHint,
                completeSingle: false,
                closeOnUnfocus: true,
                alignWithWord: true
            }
        });

        // Auto-trigger autocomplete on input - only on letters for proper filtering
        cmHtml.on("inputRead", function (cm, change) {
            if (!cm.state.completionActive &&
                change.text[0].match(/[a-zA-Z]/)) {
                CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
            }
        });
    }

    if (cssEditor) {
        cmCss = CodeMirror.fromTextArea(cssEditor, {
            lineNumbers: true,
            mode: 'css',
            theme: 'monokai',
            lineWrapping: true,
            autoCloseBrackets: true,
            extraKeys: {
                "Ctrl-Space": "autocomplete",
                "':'": completeAfterColon,
                "' '": completeAfterSpace
            },
            hintOptions: {
                completeSingle: false,
                closeOnUnfocus: true,
                alignWithWord: true
            }
        });
        cmCss.getWrapperElement().style.display = 'none';

        // Auto-trigger autocomplete on input
        cmCss.on("inputRead", function (cm, change) {
            if (!cm.state.completionActive &&
                change.text[0].match(/[a-zA-Z:-]/)) {
                CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
            }
        });
    }

    if (jsEditor) {
        cmJs = CodeMirror.fromTextArea(jsEditor, {
            lineNumbers: true,
            mode: 'javascript',
            theme: 'monokai',
            lineWrapping: true,
            autoCloseBrackets: true,
            extraKeys: {
                "Ctrl-Space": "autocomplete",
                "'.'": completeAfterDot
            },
            hintOptions: {
                completeSingle: false,
                closeOnUnfocus: true,
                alignWithWord: true
            }
        });
        cmJs.getWrapperElement().style.display = 'none';

        // Auto-trigger autocomplete on input
        cmJs.on("inputRead", function (cm, change) {
            if (!cm.state.completionActive &&
                change.text[0].match(/[a-zA-Z.]/)) {
                CodeMirror.commands.autocomplete(cm, null, { completeSingle: false });
            }
        });
    }

    // Helper functions for smart autocomplete triggers
    function completeAfter(cm, pred) {
        if (!pred || pred()) setTimeout(function () {
            if (!cm.state.completionActive)
                cm.showHint({ completeSingle: false });
        }, 100);
        return CodeMirror.Pass;
    }

    function completeIfAfterLt(cm) {
        return completeAfter(cm, function () {
            var cur = cm.getCursor();
            return cm.getRange(CodeMirror.Pos(cur.line, cur.ch - 1), cur) == "<";
        });
    }

    function completeIfInTag(cm) {
        return completeAfter(cm, function () {
            var tok = cm.getTokenAt(cm.getCursor());
            if (tok.type == "string" && (!/['"]/.test(tok.string.charAt(tok.string.length - 1)) || tok.string.length == 1)) return false;
            var inner = CodeMirror.innerMode(cm.getMode(), tok.state).state;
            return inner.tagName;
        });
    }

    function completeAfterColon(cm) {
        return completeAfter(cm, function () {
            var cur = cm.getCursor();
            return cm.getRange(CodeMirror.Pos(cur.line, cur.ch - 1), cur) == ":";
        });
    }

    function completeAfterSpace(cm) {
        return completeAfter(cm, function () {
            var tok = cm.getTokenAt(cm.getCursor());
            return tok.type == "property";
        });
    }

    function completeAfterDot(cm) {
        return completeAfter(cm, function () {
            var cur = cm.getCursor();
            return cm.getRange(CodeMirror.Pos(cur.line, cur.ch - 1), cur) == ".";
        });
    }

    // Tab switching
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;

            // Update active tab
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Show corresponding editor
            if (cmHtml) cmHtml.getWrapperElement().style.display = lang === 'html' ? 'block' : 'none';
            if (cmCss) cmCss.getWrapperElement().style.display = lang === 'css' ? 'block' : 'none';
            if (cmJs) cmJs.getWrapperElement().style.display = lang === 'js' ? 'block' : 'none';
        });
    });

    if (runBtn) {
        runBtn.addEventListener('click', () => {
            const htmlCode = cmHtml ? cmHtml.getValue() : htmlEditor.value;
            const cssCode = cmCss ? cmCss.getValue() : cssEditor.value;
            const jsCode = cmJs ? cmJs.getValue() : jsEditor.value;

            updatePreview(htmlCode, cssCode, jsCode);
            checkCode(htmlCode);
        });
    }

    if (modalClose) {
        modalClose.addEventListener('click', () => {
            modal.classList.add('hidden');
        });
    }

    // Console elements
    const consoleOutput = document.getElementById('console-output');
    const consoleLogs = document.getElementById('console-logs');

    // Listen for logs from iframe
    if (consoleOutput && consoleLogs) {
        window.addEventListener('message', (event) => {
            if (event.data.type === 'log') {
                const entry = document.createElement('div');
                entry.className = 'log-entry';
                const message = event.data.args.map(arg => {
                    if (typeof arg === 'object') return JSON.stringify(arg);
                    return String(arg);
                }).join(' ');
                entry.innerText = '> ' + message;
                consoleLogs.appendChild(entry);
                consoleOutput.classList.remove('hidden');
                consoleLogs.scrollTop = consoleLogs.scrollHeight;
            } else if (event.data.type === 'error') {
                const entry = document.createElement('div');
                entry.className = 'log-entry log-error';
                entry.innerText = '> ERROR: ' + event.data.message;
                consoleLogs.appendChild(entry);
                consoleOutput.classList.remove('hidden');
            }
        });
    }

    function updatePreview(htmlCode, cssCode, jsCode) {
        if (!preview) return;

        const doc = preview.contentDocument || preview.contentWindow.document;

        // Clear console
        if (consoleLogs) {
            consoleLogs.innerHTML = '';
            consoleOutput.classList.add('hidden');
        }

        // Console override script
        const consoleScript = `
            <script>
                (function() {
                    const originalLog = console.log;
                    const originalError = console.error;
                    
                    console.log = function(...args) {
                        window.parent.postMessage({type: 'log', args: args}, '*');
                        originalLog.apply(console, args);
                    };
                    
                    console.error = function(...args) {
                        window.parent.postMessage({type: 'error', message: args.join(' ')}, '*');
                        originalError.apply(console, args);
                    };
                    
                    window.onerror = function(msg, url, line) {
                        window.parent.postMessage({type: 'error', message: msg + ' (Line ' + line + ')'}, '*');
                    };
                })();
            <\/script>
        `;

        // Combine all code
        const fullCode = `
            ${consoleScript}
            <style>${cssCode}</style>
            ${htmlCode}
            <script>${jsCode}<\/script>
        `;

        doc.open();
        doc.write(fullCode);
        doc.close();
    }

    function checkCode(code) {
        if (!missionId) return;

        fetch('/check_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                mission_id: missionId.value
            }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showModal('MISSION ACCOMPLISHED', data.message, true);
                } else {
                    showModal('ERROR DETECTED', data.message, false);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }

    function showModal(title, message, isSuccess) {
        if (!modal) return;

        modalTitle.innerText = title;
        modalMessage.innerText = message;

        if (isSuccess) {
            modalTitle.style.color = 'var(--primary-color)';
            modalClose.classList.add('hidden');
            if (nextMissionBtn) nextMissionBtn.classList.remove('hidden');
            if (homeBtn) homeBtn.classList.remove('hidden');
        } else {
            modalTitle.style.color = 'var(--error-color)';
            modalClose.classList.remove('hidden');
            if (nextMissionBtn) nextMissionBtn.classList.add('hidden');
            if (homeBtn) homeBtn.classList.add('hidden');
        }

        modal.classList.remove('hidden');
    }
});

// Debug Emmet loading
window.addEventListener('load', function () {
    console.log("Page loaded. Checking Emmet...");
    if (window.emmet) {
        console.log("Emmet object found. Keys:", Object.keys(window.emmet));
        try {
            // Try to find the expansion function
            if (typeof emmet.expandAbbreviation === 'function') {
                console.log("emmet.expandAbbreviation exists. Testing '!'...");
                console.log("Result:", emmet.expandAbbreviation('!', { syntax: 'html' }));
            } else {
                console.log("emmet.expandAbbreviation NOT found.");
            }

            if (typeof emmet.default === 'function') {
                console.log("emmet.default exists. Testing '!'...");
                console.log("Result:", emmet.default('!', { syntax: 'html' }));
            }
        } catch (e) {
            console.error("Emmet test error:", e);
        }
    } else {
        console.error("window.emmet is undefined!");
    }
});
