def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return 0
        else:
            return 1


for i in range(2,600851475143):
    if 600851475143 % i == 0 and is_prime(int(600851475143/i)):
        print(i)
        print(600851475143/i)
        break
    else:
        print(str(i) + " nulla")
