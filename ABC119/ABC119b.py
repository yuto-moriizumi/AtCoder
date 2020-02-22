# ABC119b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
x = [list(input().split()) for _ in range(n)]
ans = 0

for i in x:
    if (i[1] == 'BTC'):
        ans += float(i[0]) * 380000
    else:
        ans += int(i[0])
print(ans)
