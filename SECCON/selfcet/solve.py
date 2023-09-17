from pwn import *

context.arch = 'amd64'
pty = process.PTY
is_local = False

elf = ELF("./xor")
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
        b *main+71
      ''')

p.interactive()
