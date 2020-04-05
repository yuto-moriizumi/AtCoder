# ABC161f


def main():
    import sys
    import math
    from collections import Counter
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    # dp=[0]*

    def prime_numbers(right):  # 素数列挙
        pn = [2]
        for L in range(3, right):
            chk = True
            for L2 in pn:
                if L % L2 == 0:
                    chk = False
            if chk == True:
                pn.append(L)
        return pn

    def prime_factorize(n):  # 素因数分解
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

   # pn = prime_numbers(math.ceil(n))
    #pf = prime_factorize(n+1)

    # for i in range(1, n + 1):
    #    if n % i == 1:
    #        print(i, prime_factorize(i))
    t = prime_factorize(n - 1)
    w = Counter(t)
    ans = 2 ** len(t)
    for i in w.most_common():
        print(i)
        ans /= 2**(i[1]-1)
    print(ans)


if __name__ == '__main__':
    main()
