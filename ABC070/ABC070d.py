# ABC070d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
cost = [10**10]*n
edge = [dict() for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    edge[a-1].update({b-1: c})
    edge[b-1].update({a-1: c})

Q, K = map(int, input().split())


def dfs(i, prev, d):
    cost[i] = d
    for j in edge[i].keys():
        if j == prev:
            continue
        dfs(j, i, d+edge[i][j])


dfs(K-1, -1, 0)

for _ in range(Q):
    x, y = map(int, input().split())
    print(cost[x-1]+cost[y-1])
