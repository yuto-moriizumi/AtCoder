n = int(input())
t = [int(input()) for _ in range(n)]


def dfs(i, sum1, sum2):
    if (i >= n):
        return max(sum1, sum2)
    return min(dfs(i+1, sum1+t[i], sum2), dfs(i+1, sum1, sum2+t[i]))


print(dfs(0, 0, 0))
