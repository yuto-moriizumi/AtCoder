n = int(input())
p = list(map(int, input().split()))

dp = [[None for i in range(sum(p)+1)] for _ in range(n+1)]


def canMake(i, v):
    if (i == 0):
        return v == 0
    if (dp[i][v] != None):
        return dp[i][v]
    # print(i)
    if (v - p[i-1] >= 0):
        dp[i][v] = canMake(i-1, v) or canMake(i-1, v-p[i-1])
    else:
        dp[i][v] = canMake(i-1, v)
    return dp[i][v]


ans = 0
for i in range(sum(p) + 1):
    if (canMake(n, i)):
        ans += 1
print(ans)
