from fractions import gcd
from functools import reduce
#from math import gcd
n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > max(a):
    print('IMPOSSIBLE')
    exit(0)
if k in a:
    print('POSSIBLE')
    exit(0)


def gcds(*numbers):
    return reduce(gcd, numbers)


if k % gcds(*a) == 0:
    print('POSSIBLE')
    exit(0)
print('IMPOSSIBLE')

# 拡張ユークリッド互除法


def xGcd(a, b, x, y) {
    if (b == 0) {
        x = 1
        y = 0
        return a
    }
    long long d = extGCD(b, a % b, y, x)
    y -= a/b * x
    return d
}
