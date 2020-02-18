f=open("challenge.exe").read()
# q1=open("data.txt","w+")
s=""
for i in range(len(f)):
	q=ord(f[i])^30
	if(q==106):
		q=0
	p=hex(q)[2:]
	if(len(p)<2):
		p='0'+p
	# q1.write(p+" ")
	s+=p
# print
# open("robot.png","wb").write(open("new").read()[::-1].decode('hex'))
open("ans.exe","wb").write(s.decode('hex'))