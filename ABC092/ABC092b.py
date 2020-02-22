# ABC092b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = x
for i in range(1, n+1):
    for j in range(1, d + 1, a[i - 1]):
        #print(i, j)
        ans += 1
print(ans)
