# ABC072d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n):
    if p[i] == i+1:
        if i == n-1:
            ans += 1
            continue
        t = p[i]
        p[i] = p[i+1]
        p[i+1] = t
        ans += 1
print(ans)
