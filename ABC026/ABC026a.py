# ABC026a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
x = 0
y = n
ans = 0
for i in range(1, n):
    ans = max(ans, i*(n-i))
print(ans)
