# ABC022a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for _ in range(n-1)]
ac = [-1]*n
ac[-1] = w

for i in range(n-1):
    ac[i] = a[i]+ac[i-1]

ans = 0

for i in ac:
    if s <= i <= t:
        ans += 1
print(ans)
