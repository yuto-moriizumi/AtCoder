# ABC079d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = 10
d = [[float("inf") for i in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０


def warshall_floyd(d):
    # d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


h, w = map(int, input().split())
for i in range(10):
    c = list(map(int, input().split()))
    for j in range(10):
        d[i][j] = c[j]
warshall_floyd(d)

a = [list(map(int, input().split())) for _ in range(h)]
cou = [0]*10
for i in a:
    for j in range(10):
        cou[j] += i.count(j)
ans = 0
for i in range(10):
    ans += cou[i]*d[i][1]
# for i in range(10):
    # print(d[i][1])
print(ans)
