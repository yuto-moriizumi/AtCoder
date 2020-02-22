n, m = map(int, input().split())
table = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    table[u-1][v-1] = True
    table[v-1][u-1] = True

visited = [False]*n


def dfs(pos, last):
    #print(pos, last)
    if (pos == last):
        return 0
    if (visited[pos] == True):
        return 1
    visited[pos] = True
    cnt = 0
    for i in range(n):
        if (i == pos or i == last):
            continue
        if (table[pos][i]):
            cnt += dfs(i, pos)
    return cnt


ans = 0
for i in range(n):
    if(not visited[i] and dfs(i, -1) == 0):
        ans += 1
print(ans)
