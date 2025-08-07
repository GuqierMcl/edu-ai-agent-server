from pathlib import Path


def find_null():
    for p in Path('.').rglob('*.py'):
        try:
            with p.open('rb') as f:
                if b'\x00' in f.read():
                    print(p)
        except Exception as e:
            print('skip', p, e)


if __name__ == '__main__':
    find_null()

# 运行后就能看到是哪个（哪些）文件含有空字节，再按之前的方法用编辑器转存为 UTF-8（无 BOM）即可。