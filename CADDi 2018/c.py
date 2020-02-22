from collections import Counter
n, p = map(int, input().split())


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


ans = 1
for i in Counter(prime_factorize(p)).most_common():
    if i[1] < n:
        break
    ans *= i[0]**(i[1]//n)
print(ans)
