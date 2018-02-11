sum = 0
fiboArr = [0 for i in range(300000)]
fiboArr[0] = 1
fiboArr[1] = 2
i = 1

while fiboArr[i] < 4000000:
    if fiboArr[i] % 2 == 0:
        sum += i

    i += 1;
    fiboArr[i] += fiboArr[i - 1] + fiboArr[i - 2]

print(sum)
print(fiboArr)
