# 文字列操作・再帰だけはPythonで出す
# from subprocess import*
# call(('pypy3', '-c', """

import random
from functools import reduce
import collections
import math


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())


if __name__ == '__main__':
    main()

# """))

alphabet = list('abcdefghijklmnopqrstuvwxyz')
# メモ
# listは遅い set最速 dict次点 listが最遅

# 二次元リスト
# [[0]*w for _ in range(h)]

# numpyの選択
# a=
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]] この行列に対して

# a[1:,1:3]は
# [[5 6
#  9 10]]
# 詳しくはABC129d.2を参照

# 素因数分解
# collections.Counter(result)で辞書形式に


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
# 素数列挙


def prime_numbers(right):
    pn = [2]
    for L in range(3, right):
        chk = True
        for L2 in pn:
            if L % L2 == 0:
                chk = False
        if chk == True:
            pn.append(L)
    return pn


# ユークリッド距離


def euclidean_distance(pos1, pos2):
    t = 0
    for i in range(len(pos1)):
        t += (pos1[i] - pos2[i]) ** 2
    return math.sqrt(t)

# 順列の個数


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

# 組み合わせ


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


# メモ化組み合わせ
dp = dict()


def combinations_countM(n, r):
    if dp.get(n) != None and dp.get(n).get(r) != None:
        return dp[n][r]
    if dp.get(n) == None:
        dp[n] = dict()
    dp[n].update({r: math.factorial(
        n) // (math.factorial(n - r) * math.factorial(r))})
    return dp[n][r]

# 重複組み合わせ


def combinations_with_replacement_count(n, r):
    return math.factorial(n+r-1) // (math.factorial(n - 1) * math.factorial(r))


# メモ化重複組み合わせ
dp = dict()


def combinations_with_replacement_countM(n, r):
    if dp.get(n) != None and dp.get(n).get(r) != None:
        return dp[n][r]
    if dp.get(n) == None:
        dp[n] = dict()
    dp[n].update({r: math.factorial(n+r-1) //
                  (math.factorial(n - 1) * math.factorial(r))})
    return dp[n][r]


# 最大公約数,最大公約数
# from fractions import gcd


def lcm_base(a, b):
    return a * b // gcd(a, b)

#from functools import reduce


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

# from fractions import gcd
#from functools import reduce


def gcds(*numbers):
    return reduce(gcd, numbers)

# 累積和
# result[i]=i番目までの累積和
# 初期値に注意（10^9が小さすぎたり、10^-9が大きすぎたりする）


def cum(array):
    result = [0]
    for i in range(len(array)):
        result.append(array[i]+result[i])
    return result

# 二分探索


def evaluate(number):
    if number <= 100:  # もっと高い値を探せ
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
