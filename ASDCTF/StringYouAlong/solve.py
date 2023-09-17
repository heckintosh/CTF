from pwn import *
from pwn import *

# Define the remote CTF server's address and port
remote_host = '0.cloud.chals.io'
remote_port = 19877

# Establish a connection to the remote server
conn = remote(remote_host, remote_port)

try:
    	# Receive the initial welcome message or any other data
		welcome_message = conn.recvline().decode().strip()
		print(welcome_message)
		conn.sendline("64")
		result = conn.recvall(timeout=1)
		print(result)
finally:
		conn.close()
