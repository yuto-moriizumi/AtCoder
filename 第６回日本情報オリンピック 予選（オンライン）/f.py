a, b = map(int, input().split())
n = int(input())
path = [[-1]*(a+1) for _ in range(b+1)]
for _ in range(n):
    x, y = map(int, input().split())
    path[y][x] = 0


def dfs(i, j):
    if path[i][j] == 0:
        return 0
    if i == b and j == a:
        return 1
    if i == b:
        path[i][j] = dfs(i, j+1)
        return path[i][j]
    if j == a:
        path[i][j] = dfs(i+1, j)
        return path[i][j]
    path[i][j] = dfs(i+1, j)+dfs(i, j+1)
    return path[i][j]


print(dfs(1, 1))
# print(path)
