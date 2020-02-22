# ABC139f
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    point = [xy[i][0], xy[i][1]]
    for j in range(n):
        if (i == j):
            continue
        if (xy[i][0] * xy[j][0] + xy[i][1] * xy[j][1] >= 0):
            point[0] += xy[j][0]
            point[1] += xy[j][1]
    ans = max(ans, point[0] ** 2 + point[1] ** 2)
print(math.sqrt(ans))
