MOONIE - open index.html in Chrome (double-click works).
Edit numbers/messages in game-config.json and real events in solar-events.json, then run:  python3 build.py
(if you use VS Code Live Server, edits show without build.py)
Test shortcut: index.html?event=4&emergency=2&skip=1  -> pick solar event id, flare day, skip intro

HUMAN VOICE (Gemini)
- Raed's lines are played from assets/voice/*.wav. Make them once with: python make_voices.py (needs a free GEMINI_API_KEY, see the top of that file).
- If a line has no file, the game uses the browser's built-in voice instead.
- If you change any spoken text in game-config.json or the game, ask for an updated voices.json.
