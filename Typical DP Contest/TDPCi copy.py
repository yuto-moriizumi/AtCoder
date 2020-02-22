unchi = input()
n = len(unchi)
# print(unchi.split('ww'))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(3, n+1):
    for l in range(n-i+1):
        if i == 3:
            if unchi[l:l+i] == 'iwi':
                dp[l][l+i] = 3
            continue
        for mid in range(1, i):
            dp[l][l+i] = max(dp[l][l+i], dp[l][l+mid]+dp[l+mid][l+i])
        if i % 3 == 0:
            for mid in range(1, i, 3):  # midはwの位置
                #print(l, l+mid, l+i)
                #print(dp[l+1][l+mid], dp[l+mid+1][l+i])
                # print(dp[l+1][l+mid], unchi[l+1:l+mid],
                #      dp[l+mid+1][l+i-1], unchi[l+mid+1:l+i-1])
                # if(unchi[l+mid+1:l+i-1] == 'iiiwiw'):
                #    print()
                if dp[l+1][l+mid] != mid-1 or dp[l+mid+1][l+i-1] != i-mid-2:
                    continue
                # print('hi')
                dp[l][l+i] = max(dp[l][l+i], (mid-1)+(i-mid-2)+3)
print(dp[0][n]//3)
# print(dp)
