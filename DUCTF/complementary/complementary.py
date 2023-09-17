flag = open('./flag.txt', 'rb').read().strip()
print(flag)
m1 = int.from_bytes(flag[:len(flag)//2])
m2 = int.from_bytes(flag[len(flag)//2:])
print(m1)
print(m2)
n = m1 * m2
print(n)
