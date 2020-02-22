# ABC014b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, x = map(int, input().split())
a = list(map(int, input().split()))
i = 0
ans = 0
while (x > 0):
    bit = x & 1
    if bit == 1:
        ans += a[i]
    x = x >> 1
    i += 1
print(ans)
