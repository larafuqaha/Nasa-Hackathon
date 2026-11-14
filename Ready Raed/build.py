import re,json,pathlib
d=pathlib.Path(__file__).parent
src=(d/'src.html').read_text()
src=re.sub(r'(?<![\w.#])(-?\d+(?:\.\d+)?)u(?![\w])',r'calc(var(--u)*\1)',src)
src=src.replace('__CFG__',(d/'game-config.json').read_text()).replace('__EVENTS__',(d/'solar-events.json').read_text())
(d/'index.html').write_text(src)
print('built',len(src))
