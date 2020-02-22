import copy
island = [list(input()) for _ in range(10)]

n = 0
for i in range(10):
    n += island[i].count('o')


def dfs(x, y):
    if (x < 0 or 10 <= x or y < 0 or 10 <= y or island[y][x] == 'x'):
        return 0
    island[y][x] = 'x'
    return 1 + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x, y + 1)


island2 = copy.deepcopy(island)

for i in range(10):
    for j in range(10):
        island = copy.deepcopy(island2)
        if(island[i][j] != 'o'):
            island[i][j] = 'o'
            t = dfs(j, i)
            if (t == n+1):
                print('YES')
                exit()
        else:
            t = dfs(j, i)
            if (t == n):
                print('YES')
                exit()
print('NO')
