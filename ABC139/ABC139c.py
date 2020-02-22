# ABC139c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

ans = 0
count = 0

for i in range(1, n):
    if (h[i] <= h[i - 1]):
        count += 1
    else:
        ans = max(count, ans)
        count = 0
ans = max(count, ans)
print(ans)