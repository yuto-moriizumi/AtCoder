# ABC143e
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, l = map(int, input().split())
# 距離,直前の頂点
d = [[10 ** 10] * n for _ in range(n)]
nex = [[i for i in range(0, n)] for _ in range(n)]
# print(nex)
for _ in range(m):
    a, b, c = map(int, input().split())
    if c <= l:
        d[a-1][b-1] = c
        d[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                nex[i][j] = nex[i][k]
q = int(input())
ans = []
for _ in range(q):
    s, t = map(int, input().split())
    if d[s - 1][t - 1] >= 10 ** 10:
        ans.append(-1)
        continue
    ans.append([s - 1, t - 1, d[s - 1][t - 1], l, (d[s - 1][t - 1]/l)])


def printPath3(start, goal):
    fuel = l
    ans = 0
    cur = start
    while (cur != goal):
        # print(cur)
        fuel -= d[cur][nex[cur][goal]]
        if (fuel < 0):
            ans += 1
            fuel = l-d[cur][nex[cur][goal]]
        cur = nex[cur][goal]
    # print(goal)
    return ans


for i in ans:
    # print(i)
    if i != -1:
        print(printPath3(i[0], i[1]))
    else:
        print(-1)
