# ABC073d
import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, _ = map(int, input().split())
d = [[float("inf") for i in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０
r = list(map(int, input().split()))


def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
warshall_floyd(d)

ans = 10**9
for i in itertools.permutations(r, len(r)):
    t = 0
    for j in range(1, len(i)):
        t += d[i[j]-1][i[j-1]-1]
    #print(i, t)
    ans = min(ans, t)
print(ans)
