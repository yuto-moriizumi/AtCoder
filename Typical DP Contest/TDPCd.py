n, d = map(int, input().split())

# dp[x][y][z] 素因数に2がx個、3がy個、5がz個含まれているパターンの数

dp = [[[[0] * 50 for _ in range(50)] for i in range(100)] for j in range(n+1)]

cx = 0
cy = 0
cz = 0
while (d % 2 == 0):
    cx += 1
    d = d // 2
while (d % 3 == 0):
    cy += 1
    d = d // 3
while (d % 5 == 0):
    cz += 1
    d = d//5
if (d > 1):
    print(0)
    exit()

dp[0][0][0][0] = 1

for i in range(n):
    for x in range(min(100, cx+1)):
        for y in range(min(50, cy+1)):
            for z in range(min(50, cz+1)):
                # if (dp[i + 1][x][y][z] == 0):
                # continue
                dp[(i + 1)][min(x, cx)][min(y, cy)
                                        ][min(z, cz)] += dp[i][x][y][z]/6
                dp[(i + 1)][min(x+1, cx)][min(y, cy)
                                          ][min(z, cz)] += dp[i][x][y][z]/6
                dp[(i + 1)][min(x, cx)][min(y+1, cy)
                                        ][min(z, cz)] += dp[i][x][y][z]/6
                dp[(i + 1)][min(x+2, cx)][min(y, cy)
                                          ][min(z, cz)] += dp[i][x][y][z]/6
                dp[(i + 1)][min(x, cx)][min(y, cy)
                                        ][min(z+1, cz)] += dp[i][x][y][z]/6
                dp[(i + 1)][min(x+1, cx)][min(y+1, cy)
                                          ][min(z, cz)] += dp[i][x][y][z]/6

#print(cx, cy, cz)
print(dp[n][cx][cy][cz])
