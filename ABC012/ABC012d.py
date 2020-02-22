# ABC012d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
d = [[10**8]*n for i in range(n)]
for i in range(n):
    d[i][i] = 0  # 自身のところに行くコストは０


def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


for _ in range(m):
    a, b, t = map(int, input().split())
    d[a-1][b-1] = t
    d[b-1][a-1] = t
warshall_floyd(d)

ans = 10**9
for i in d:
    ans = min(ans, max(i))
print(ans)
