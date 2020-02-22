import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = 1
r = n
for _ in range(m):
    a, b = map(int, input().split())
    l = max(l, a)
    r = min(r, b)
ans = r - l + 1
if (ans < 0):
    ans = 0
print(ans)
