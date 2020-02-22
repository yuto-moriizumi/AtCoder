# ABC024b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = t*n
for i in range(1, n):
    if a[i]-a[i-1] < t:
        ans -= t-(a[i]-a[i-1])
print(ans)
