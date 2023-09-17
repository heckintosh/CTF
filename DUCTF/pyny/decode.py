#!/usr/bin/python3
with open("test.py", "rb") as f:
    data = f.read().strip()

repl = {a: b for a, b in zip(
    'Ьаеорсухѕіјѡѵһ',
    'baeopcyxsijwvh')}

try:
    unreplaced = set()
    while b'-' in data:
        data = data.decode('punycode')
        for char in data:
            if ord(char) > 0x80:
                unreplaced.add(char)
        for a, b in repl.items():
            data = data.replace(a, b)
        data = bytearray(data, 'ascii')
finally:
    print(''.join(sorted(unreplaced)))
    print(data)