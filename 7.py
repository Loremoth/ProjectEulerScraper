p=[2]
prime=True
i=1
n=3

while(i<10001):
	for j in p:
		if n%j==0:
			prime=False
	
	if prime:
		p.append(n)
		i += 1
		print(i)
	
	n+=2
	prime = True

print(n)