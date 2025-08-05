from pathlib import Path

for p in Path('.').rglob('*.py'):
    try:
        with p.open('rb') as f:
            if b'\x00' in f.read():
                print(p)
    except Exception as e:
        print('skip', p, e)