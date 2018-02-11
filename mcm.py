def mcm(x,y):
	ma=max(x,y)
	mi=min(x,y)
	i=2
	r=ma
	
	while(r%mi!=0):
		r=ma*i
		i+=1
	
	return r
	
def mcm(x, y, z):
	i=2
	r=x
	while r%y!=0 or r%z!=0:
		r=x*i
		i+=1
	
	return r
		

for i in range(1,11):
	for j in range(1, 11):
		for k in range(1,11):
			print("uno: " + str(mcm(i,mcm(j,k,1),1)))
			print("due: " + str(mcm(mcm(i,j,1),k,1)))
			print("tre: " + str(mcm(i,j,k)))

