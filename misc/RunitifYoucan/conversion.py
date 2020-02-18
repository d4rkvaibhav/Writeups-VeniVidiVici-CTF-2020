f=open("challenge.exe").read()
s=""
for i in range(len(f)):
 q=ord(f[i])^30
 if(q==106):
  q=0
 p=hex(q)[2:]
 if(len(p)<2):
  p='0'+p
 s+=p
open("ans.exe","wb").write(s.decode('hex'))
