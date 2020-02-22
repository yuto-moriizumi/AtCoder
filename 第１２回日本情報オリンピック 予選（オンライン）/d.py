D, N = map(int, input().split())
t = [int(input()) for _ in range(D)]
a = [list(map(int, input().split())) for _ in range(N)]

# d日目を見ていて最後にlastCloth番目の服を着た、
dp = [[-1]*N for _ in range(D)]
# print(dp)


def dfs(d, lastCloth):
    #print(d, lastCloth)
    if(d >= D):
        return 0
    if(dp[d][lastCloth] != -1):
        return dp[d][lastCloth]
    ans = 0
    for i in range(N):
        if(not a[i][0] <= t[d] <= a[i][1]):
            continue
        dif = abs(a[i][2]-a[lastCloth][2]) if lastCloth != -1 else 0
        ans = max(ans, dfs(d+1, i)+dif)
    dp[d][lastCloth] = ans
    return ans


print(dfs(0, -1))
