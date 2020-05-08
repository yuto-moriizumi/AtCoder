# ABC163d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    MOD = 10**9+7

    def dump(*args):
        sys.stderr.write(str(args))

    N, K = map(int, input().split())
    import math

    def c_count(n, r):  # 組み合わせ
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    ans = c_count(N + 1, K) % MOD

    def factorial(n, p, mod=None):  # n^p 繰り返し二乗法
        if (p <= 1):
            if mod != None:
                return n**p % mod
            return n**p
        if (p % 2 == 0):
            if mod != None:
                return factorial(n, p // 2)**2 % mod
            return factorial(n, p // 2) ** 2
        if mod != None:
            return factorial(n, p - 1) * n % mod
        return factorial(n, p - 1) * n

    def modinv(a, mod=10**9+7):
        return pow(a, mod - 2, mod)

    # nCr mod m
    # modinvが必要
    # rがn/2に近いと非常に重くなる

    def combination(n, r, mod=10**9+7):
        r = min(r, n-r)
        res = 1
        for i in range(r):
            res = res * (n - i) * modinv(i+1, mod) % mod
        return res

    # print()
    #print(factorial(2, N + 1, MOD) - ans)

    #ans = factorial(2, N + 1, MOD)

    # for i in range(K):
    #    ans -= c_count(N + 1, i) % MOD
    # print(ans)

    ans = 0
    t = 0
    for i in range(1, N + 1):
        t += combination(N + 1, i) - combination(N - 1, i - 1) + 1
    print(t)
    for i in range(1, K):
        wa = combination(N + 1, i) - combination(N - 1, i - 1) + 1
    print(wa)
    for i in range(K, N+1):
        # ans += #combination(N + 1, i)  # -combination(N - 1, i-1)+1
        #ans += combination(N - 1, i-1)+1
        ans += 1
    # print(ans)  # +1
    print(factorial(2, N, MOD)-factorial(2, K-1, MOD)+ans-1)


if __name__ == '__main__':
    main()
