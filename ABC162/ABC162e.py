# ABC162e


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, k = map(int, input().split())

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
    import math

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

    def c_count(n, r):  # 組み合わせ
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    pn = prime_numbers(k+1)
    d = dict()

    def factorial(n, p, mod=1):  # n^p 繰り返し二乗法
        if (p <= 1):
            return n**p % mod
        if (p % 2 == 0):
            return factorial(n, p // 2)**2 % mod
        return factorial(n, p - 1) * n % mod

    for i in range(2, k + 1):
        p = min(prime_factorize(i))
        if d.get(p) == None:
            d[p] = 0
        d[p] += 1

    ans = 0
    kosu = 0
    for key in d:
        print(key, d[key])
        t = 0
        for i in range(1, min(n, d[key]) + 1):
            t += c_count(d[key], i)
        ans += t * key
        kosu += t
    print(k**n-kosu+ans)


if __name__ == '__main__':
    main()
