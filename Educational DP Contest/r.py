def Mmul(a, b):  # 行列の積
    # [ｍ×ｎ型][ｎ×ｐ型]
    m = len(a)
    n = len(a[0])
    if len(b) != n:
        raise ValueError('列と行の数が一致しません')
    p = len(b[0])
    ans = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                ans[i][j] += a[i][k]*b[k][j] % MOD
    return ans


def Mfactorial(n, p):  # n^p 繰り返し二乗法+行列の積
    if (p == 1):
        return n
    if (p % 2 == 0):
        t = Mfactorial(n, p // 2)
        return Mmul(t, t)
    return Mmul(Mfactorial(n, p - 1), n)


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
MOD = 10**9+7
print(sum([sum(i) % MOD for i in Mfactorial(a, k)]) % MOD)
