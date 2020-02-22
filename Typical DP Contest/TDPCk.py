import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
circle = []
for i in range(n):
    x, r = map(int, input().split())
    circle.append([x-r, x+r, i])
circle.sort()
# print(circle)

# dp[i]=長さがi+1の最長増加部分列の最後の要素のうち最も小さい数
dp = [10**10]*n

for i in range(n):
    dp[bisect.bisect_left(dp, -circle[i][1])] = -circle[i][1]
# print(dp)
print(n-dp.count(10**10))
