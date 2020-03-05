# ABC009d
import numpy as np
import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 3次正方行列
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

a = np.array([[1, 1], [1, 0]])

b = np.array([[1, 0]])

c = np.matrix([[1, 2], [3, 4]])

d = np.matrix([[5, 6], [7, 8]])
print(c)
print(d)
print(c*d)


def mul(a, b):  # 行列の積
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
                ans[i][j] |= a[i][k] & b[k][j]
    return ans


def factorial(n, p):  # n^p 繰り返し二乗法
    if (p == 1):
        return n
    if (p % 2 == 0):
        t = factorial(n, p // 2)
        return mul(t, t)
    return mul(factorial(n, p - 1), n)


print(mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

print(mul(factorial([[1, 1], [1, 0]], 10), [[1], [0]]))

K, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

the1 = [list()]
for i in c:
    the1[0].append(i)
for i in range(K-1):
    the1.append([0] * K)
    the1[i+1][i] = (1 << 33) - 1
the2 = []
for i in a[::-1]:
    the2.append([i])
print(the1)
print(the2)
#print(mul(the1, the2))
print(factorial(the1, 5))
ans = 0
for i in mul(factorial(the1, 5), the2):
    for j in i:
        ans ^= j
print(ans)
