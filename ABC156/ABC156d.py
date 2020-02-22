# ABC156d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    import math
    MOD = 10**9+7

    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

    n, a, b = map(int, input().split())
    # print(2**n)
    # print(2**n % MOD-1-combinations_count(n, a)-combinations_count(n, b))

    def pow_k(x, n):
        if n == 0:
            return 1

        K = 1
        while n > 1:
            if n % 2 != 0:
                K *= x
            x *= x
            n //= 2

        return K % MOD * x % MOD

    def cmb(n, r):
        if n - r < r:
            r = n - r
        if r == 0:
            return 1
        if r == 1:
            return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2, r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1, r, p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result = result*int(numerator[k]) % MOD

        return result % MOD

    _FAC_TABLE = [1, 1]

    def factorial(n):
        if n < len(_FAC_TABLE):
            return _FAC_TABLE[n]

        last = len(_FAC_TABLE) - 1
        total = _FAC_TABLE[last]
        for i in range(last + 1, n + 1):
            total *= i
            _FAC_TABLE.append(total)
    # print(factorial(n))

    def mod_fact(n, p, e):
        e = 0
        if n == 0:
            return 1
        res = mod_fact(n / p, p, e)
        e += n / p
        if n / p % 2 != 0:
            return res * (p - fact[n % p]) % p
        return res*fact[n % p] % p

    def range_prod(lo, hi):
        if lo+1 < hi:
            mid = (hi+lo)//2
            return range_prod(lo, mid) * range_prod(mid+1, hi)
        if lo == hi:
            return lo
        return lo*hi

    def treefactorial(n):
        if n < 2:
            return 1
        return range_prod(1, n)

    # print(treefactorial(n))

    def comb(n, k):
        deno = 1
        num = 1
        result = 1
        # set the value of deno and num bounds
        if k > n - k:
            num_val = k + 1
            den_val = n - k
        else:
            num_val = n - k + 1
            den_val = k
        i = n
        # calculate n * (n - k) *....* (n-num_value))
        while i != num_val - 1:
            if i == 0:
                result *= 1
            else:
                result *= i
            if i == num_val:
                num = result
            i -= 1
        i = 0
        result = 1
        # calculate den_val! (factorial of denominator)
        while i != den_val + 1:
            if i == 0:
                result *= 1
            else:
                result *= i
            if i == den_val:
                deno = result
            i += 1
        ans = num/deno
        return ans
    # print(cmb(n, a))
    def prepare(n, MOD):

        # n! の計算
        f = 1
        for m in range(1, n + 1):
            f *= m
            f %= MOD
        fn = f

        # n!^-1 の計算
        inv = pow(f, MOD - 2, MOD)
        # n!^-1 - 1!^-1 の計算
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= MOD
            invs[m - 1] = inv

        return fn, invs
    #pre = prepare(n, MOD)
    #print(pre[0]*pre[1][1] % MOD)
    # print(cmb(n, b) % MOD)
    # print(cmb(n, a))
    # ans = pow_k(2, n) - 1 - cmb(n, a) - cmb(n, b)
    # while ans < 0:
    #    ans += MOD
    # print(ans)

    def coomb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    mod = 10**9+7  # 出力の制限
    N = 10**4
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    #print(coomb(n, a, MOD))

    def factorial_cor(n, r):
        fact = 1
        for i in range(r):
            fact = fact*(n-i) % MOD
        return fact
    #print(factorial_cor(10, 1) % MOD)

    def commb(n, r):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        cor = factorial_cor(n, r) % MOD
        cor += MOD
        return cor // math.factorial(r) % MOD

    print(pow_k(2, n) % MOD - 1-commb(n, a)-commb(n, b) % MOD)


if __name__ == '__main__':
    main()
