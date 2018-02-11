max = 0


def is_palindrome(a):
    for i in range(str(a).__len__()):
        # print(str(a)[i])
        # print(str(a)[-1-i])
        if str(a)[i] != str(a)[-1 - i]:
            return 0

    return 1


for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j) and (i * j) > max:
            max = i * j
            print(i * j)
        # else:
        #     print(str(i*j)+" nulla")

x = 123456
print(x)
