from pwn import *
import os

context.arch = 'amd64'
pty = process.PTY
is_local = False
is_remote = False

elf_local = ELF("/home/kali/CTF/PCTF/print_shop/printshop")
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

#debug(cmd='''
#        b *adminBook+114
#      ''')

