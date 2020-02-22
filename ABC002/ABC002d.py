# ABC002d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
table = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    table[x][y] = True
    table[y][x] = True

# print(table)
clique = set()


def dfs(i, cnt):
    if (i >= n):
        for j in clique:
            for k in clique:
                if (j == k):
                    continue
                #print(j, k)
                if (not table[j][k]):
                    return 0
        return cnt
    # 入れる場合
    clique.add(i+1)
    ireru = dfs(i + 1, cnt + 1)
    # 入れない場合
    clique.discard(i+1)
    irenai = dfs(i + 1, cnt)
    return max(ireru, irenai)


print(max(1, dfs(0, 0)))
