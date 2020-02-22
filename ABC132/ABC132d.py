# ABC132d
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
MOD = 10**9+7


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, k = map(int, input().split())
ans = []
ans.append(n-k+1)
for i in range(2, k):
    ans.append(ans[i - 2] * (n - k))
for i in ans:
    print(i % MOD)
try:
    print(combinations_count(n-k+1, k) % MOD)
except:
    print(0)
