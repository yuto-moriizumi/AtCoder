# ABC032c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]

if 0 in s:
    print(n)
    exit(0)

left = 0
now = 1
ans = 0

for right in range(1, n+1):
    now *= s[right-1]
    if now <= k:
        ans = max(ans, right - left)
        continue
    while (now > k and left < right):
        now = now/s[left]
        left += 1
print(ans)
