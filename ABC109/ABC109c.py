# ABC109c
from fractions import gcd
from functools import reduce
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
diff = []
for i in range(1, n+1):
    diff.append(x[i]-x[i-1])
# print(diff)


def gcds(*numbers):
    return reduce(gcd, numbers)


print(gcds(*diff))
