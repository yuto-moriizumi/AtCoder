alphabet = list('abcdefghijklmnopqrstuvwxyz')


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


def euclidean_distance(pos1, pos2):  # ユークリッド距離
    t = 0
    for i in range(len(pos1)):
        t += (pos1[i] - pos2[i]) ** 2
    return math.sqrt(t)


def p_count(n, r):  # 順列の個数
    return math.factorial(n) // math.factorial(n - r)


def c_count(n, r):  # 組み合わせ
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def h_count(n, r):  # 重複組み合わせ
    return math.factorial(n+r-1) // (math.factorial(n - 1) * math.factorial(r))


class Combination:  # メモ化組み合わせ
    def __init__(self):
        super().__init__()
        self.dp = dict()

    def count(n, r):
        if dp.get((n, r)) != None:
            return dp[(n, r)]
        dp[(n, r)] = c_count(n, r)
        return dp[(n, r)]


class Homogeneous:  # メモ化重複組み合わせ
    def __init__(self):
        super().__init__()
        self.dp = dict()

    def count(n, r):
        if dp.get((n, r)) != None:
            return dp[(n, r)]
        dp[(n, r)] = h_count(n, r)
        return dp[(n, r)]


# 最大公約数,最大公約数
# from fractions import gcd
#from functools import reduce

def lcm_base(a, b):
    return a * b // gcd(a, b)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def gcds(*numbers):
    return reduce(gcd, numbers)


def cum(array):  # result[i]=i番目まで（1-indexed）の累積和
    result = [0]
    for i in range(len(array)):
        result.append(array[i]+result[i])
    return result


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

# 二分探索


def evaluate(number):
    if number < 100:  # もっと高い値を探せ
        return 1
    if number == 100:  # まさにこの値
        return 0
    if number > 100:  # もっと低い値を探せ
        return - 1


def binary_search(low, high):
    lowest = low
    highest = high
    while low <= high:  # high-low >= 10**-12 ←これ以下の誤差を許容
        mid = (low + high) // 2
        guess = evaluate(mid)
        if guess == 0:
            return [mid, mid]
        if guess < 0:
            high = mid - 1  # 連続値の場合mid
            highest = mid
        else:
            low = mid + 1  # 連続値の場合mid
            lowest = mid

    return [lowest, highest]


def compr_coord(array):  # 座標圧縮 n=|array|,O(NlogN) 4,120,121→0,1,2
    toAfter = dict()
    b = [(array[i], i) for i in range(len(array))]
    b.sort()
    toBefore = [0]*(len(array)+1)
    for i in range(len(array)):
        toAfter[array[b[i][1]]] = i
        toBefore[i] = array[b[i][1]]
    return (toBefore, toAfter)


def alphabetToZeroIndexed(alphabet):
    return ord(alphabet)-97


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
                ans[i][j] += a[i][k]*b[k][j]
    return ans


def Mfactorial(n, p):  # n^p 繰り返し二乗法+行列の積
    if (p == 1):
        return n
    if (p % 2 == 0):
        t = factorial(n, p // 2)
        return Mmul(t, t)
    return Mmul(factorial(n, p - 1), n)


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
