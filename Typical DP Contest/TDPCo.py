import math
n = list(map(int, input().split()))
MOD = 10**9+7
n.sort(reverse=True)
# print(n)

# dp[i][j] := i 番目の文字まで見た時，同じ文字が連続している場所が j 箇所あるような場合の数

dp = [[0]*sum(n) for k in range(len(n))]

ruisekiwa = [0]
for i in range(1, len(n)+1):
    ruisekiwa.append(ruisekiwa[i-1]+n[i-1])
# print(ruisekiwa)


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


dp[0][0] = 1
for i in range(len(n)):
    for j in range(ruisekiwa[i+1]+1):
        for k in range(1, n[i]+1):
            for l in range(min(j, k)+1):
                t = combinations_count(n[i]-1, k-1)
                t = (t*combinations_count(j, l)) % MOD
                t = (t*combinations_count(ruisekiwa[i+1]-j+1, k-l)) % MOD
                t = (t*dp[i][j]) % MOD
                dp[i+1][j-l+n[i]-k] = (dp[i+1][j-l+n[i]-k]+t) % MOD


print(dp[len(n)-1][0])
print(dp)
