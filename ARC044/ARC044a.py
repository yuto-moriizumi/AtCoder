n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ar = prime_factorize(n)
# print(ar)
if n == 1:
    print('Not Prime')
    exit(0)
if len(ar) == 1:
    print('Prime')
    exit(0)
if int(str(n)[-1]) % 2 == 1 and int(str(n)[-1]) != 5:
    if sum(tuple(map(int, list(str(n))))) % 3 != 0:
        print('Prime')
        exit(0)
print('Not Prime')
