"""Make Raed's human-sounding voice files with Gemini text-to-speech.

1. Get a free key at https://aistudio.google.com/apikey
2. Run (Windows PowerShell):  $env:GEMINI_API_KEY="your-key"; python make_voices.py
   Run (Mac/Linux):          GEMINI_API_KEY=your-key python make_voices.py
3. Files appear in assets/voice/ and the game plays them automatically.
   (If a file is missing the game falls back to the browser's robot voice.)

The key is only used here on your computer. It is NOT put inside the game.
Raed is male, so VOICE is a male voice. Other male voices to try: Fenrir (excitable),
Achird (friendly), Charon (informative), Orus (firm), Sadachbia (lively).
"""
import base64, json, os, sys, time, urllib.request, urllib.error, wave

VOICE = "Puck"   # a male voice (upbeat). Other male options: Fenrir, Charon, Orus, Achird
STYLE = "Say this in a warm, excited, friendly voice, like a young male astronaut talking to kids: "
MODEL = "gemini-2.5-flash-preview-tts"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "voice")
KEY = os.environ.get("GEMINI_API_KEY")
if not KEY:
    sys.exit("Set GEMINI_API_KEY first (see the top of this file).")
os.makedirs(OUT, exist_ok=True)
lines = json.load(open(os.path.join(HERE, "voices.json"), encoding="utf-8"))
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

def tts(text):
    body = {"contents": [{"parts": [{"text": STYLE + text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}}}}
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json", "x-goog-api-key": KEY})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    return base64.b64decode(data["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])

ok = 0
for i, ln in enumerate(lines, 1):
    path = os.path.join(OUT, ln["key"] + ".wav")
    if os.path.exists(path):
        ok += 1; continue
    for attempt in range(6):
        try:
            pcm = tts(ln["text"])
            with wave.open(path, "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(pcm)
            print(f"[{i}/{len(lines)}] ok  {ln['text'][:60]}"); ok += 1; break
        except urllib.error.HTTPError as e:
            if e.code == 429:      # free-tier speed limit: wait and retry
                print(f"[{i}/{len(lines)}] rate limit, waiting 45 s ({attempt+1}/6)..."); time.sleep(45)
            else:
                print(f"[{i}/{len(lines)}] HTTP {e.code}: {e.read()[:200]}"); time.sleep(5)
        except Exception as e:
            print(f"[{i}/{len(lines)}] {e}"); time.sleep(5)
    time.sleep(8)                  # go slowly to stay under the free limit
missing = [l["text"][:50] for l in lines if not os.path.exists(os.path.join(OUT, l["key"] + ".wav"))]
print(f"Done: {len(lines)-len(missing)}/{len(lines)} voice files in assets/voice/")
if missing: print("Still missing (run the script again later, it keeps the ones it has):", *missing, sep="\n  ")