# Ready, Raed?

**A Moon-base survival game for kids aged 7–12.** Built by Team **WaNasa** for the NASA Space Apps Challenge 2026, challenge: *Build a Junior Astronaut Mission Trainer*.

**[▶ Play the game](https://larafuqaha.github.io/Nasa-Hackathon/)** · Free · Runs in the browser · No install

---

## What is it?

You are Raed's mission control. Help astronaut Raed survive **5 days** on the Moon by managing **air, water, food and power**, and protect him from a **real NASA solar storm**.

**No choice is free:**
- Water for plants is water Raed can't drink.
- Making oxygen uses power and water.
- Power for the shelter is power you can't use for air or plants.

When a supply runs out, Raed loses a heart, and the day report explains why. Kids learn real space trade-offs by trying, failing and trying again.

## How to play

1. Pick a real NASA solar storm.
2. Each day, open the **Power Room** and plan how to use power (air machine, plant lights), then save your plan.
3. In the **Greenhouse**, tap **+** on plants to water them and grow food (they need light and water).
4. In the **Air Room**, tap **+ Oxygen** to split water (H₂O) and make extra air.
5. When the storm warning comes, prepare the **Radiation Shelter** and get Raed inside before the countdown ends.
6. Survive 5 days with at least one heart.

## Real NASA data

| What | Source |
|---|---|
| Solar flares and sun-spark (SEP) records, e.g. the X3.9 flare of 10 May 2024 | [NASA DONKI](https://kauai.ccmc.gsfc.nasa.gov/DONKI/) — archived data, not live |
| Oxygen and water use per astronaut per day (about 0.8 kg and 2.5 L) | [NASA Life Support Baseline Values and Assumptions Document (BVAD), 2018](https://ntrs.nasa.gov/citations/20180001338) |

Example event page: [X3.9 flare, 10 May 2024](https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/FLR/30666/2)

## What is real and what is simplified

We label this inside the game too.

**Real**
- The solar events (dates, flare classes, linked sun-spark records) come from DONKI.
- Air and water use follow NASA life-support planning values.
- Light from a flare reaches the Moon in minutes, while sun sparks (fast particles) can take hours. The Earth–Moon signal time shown in the game (1.3 seconds) is real.

**Simplified (game values)**
- Power numbers, plant growth and water use for plants.
- The storm countdown: the real storm took about 6 hours to arrive, and the game gives seconds.
- **Dice rule:** if DONKI has no sun-spark record for a flare, the game uses a chance (20% mild, 50% medium, 80% strong) to decide whether sun sparks arrive. These percentages are our own game numbers, not NASA values.
- Game levels (mild / medium / strong) are our labels based on flare class, not NASA ratings.

## Run it locally

No server needed. Download the repository and open `index.html` in a browser.

## Project files

| File | Purpose |
|---|---|
| `index.html` | The game (everything built in) |
| `src.html` | Editable source of the game |
| `game-config.json` | Game numbers and messages |
| `solar-events.json` | The NASA DONKI events used |
| `build.py` | Builds `index.html` from `src.html` + the JSON files (`python build.py`) |
| `assets/` | Art and the voice files (`assets/voice/`) |
| `make_voices.py`, `voices.json` | Script that creates Raed's voice with Gemini (needs your own API key, never commit it) |

## Technology

HTML, CSS and JavaScript (no backend), Web Audio for sound effects, NASA DONKI data saved as JSON.

## Use of Super Intelligence (SI)

- **Code and scripts:** Claude (Anthropic) helped write and test the game code and the presentation script. The team directed the design and tested the result.
- **Audio:** Raed's voice lines are SI-generated with Google Gemini text-to-speech.
- No NASA logos, flags or mission identifiers are used.

## Next steps

Test with children · Arabic version · more missions · Mars Level · two-way Earth messages

## Team WaNasa

Duha Shehadeh · Lara Fuqaha · Taima Nasser · Sadeel Ghithan · Maysan Wadi · Bashar Zein
