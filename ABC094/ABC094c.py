# ABC094c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    x[i] = (x[i], i)
x.sort()

ans = [-1]*n

ind = n//2
for i in range(n):
    if i <= n//2-1:
        ans[x[i][1]] = x[n//2][0]
    else:
        ans[x[i][1]] = x[n//2-1][0]
print(*ans, sep='\n')
