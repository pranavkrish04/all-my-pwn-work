#!/usr/bin/python3
from pwn import *

exe = './'
elf = context.binary = ELF(exe)
# libc = ELF("")

def start(argv=[], *a, **kw):

    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

p = start()



p.interactive()
