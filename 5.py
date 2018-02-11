def mcm(x,y):
	ma=max(x,y)
	mi=min(x,y)
	i=2
	r=ma
	
	while(r%mi!=0):
		r=ma*i
		i+=1
	
	return r


m = 2520

for i in range(11,21):
	m=mcm(m,i)
	
for i in range(1,21):
	print(m%i)
	
print (m)
	