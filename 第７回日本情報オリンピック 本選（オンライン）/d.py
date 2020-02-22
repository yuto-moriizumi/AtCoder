n, m = map(int, input().split())
WIDTH = 5
stones = [[-1]*WIDTH for _ in range(n)]
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(0, t[0]*2, 2):
        stones[i][t[j+1]-1] = t[j+2]
print(stones)


def dfs(i, j, tobaseru):
    if i == n-1:
        return 0
    print(i, j, tobaseru)
    cost = 0
    for k in range(WIDTH):
        if stones[i+1][k] == -1:
            continue
        cost = min(cost, dfs(i+1, k, tobaseru) +
                   (stones[i][j]+stones[i+1][k])*abs(j-k))
    if tobaseru == 0 or i >= n-2:
        return cost
    for k in range(WIDTH):
        if stones[i+2][k] == -1:
            continue
        cost = min(cost, dfs(i+2, k, tobaseru-1) +
                   (stones[i][j]+stones[i+2][k])*abs(j-k))
    return cost


print(dfs(0, 0, m))
