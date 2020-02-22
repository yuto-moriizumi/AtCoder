n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 10**9

for i in range(n):
    for j in range(i+1, n):
        p = xy[j][0] - xy[i][0]
        q = xy[j][1] - xy[i][1]
        cost = 0
        b = set()
        # print('p,q='+str(p)+','+str(q))
        for k in xy:
            if (p == 0):
                seppen = k[0]
            elif (q == 0):
                seppen = k[0]
            else:
                seppen = round(k[1] - k[0] * q / p, 10)
            # print(seppen)
            if (not seppen in b):
                cost += 1
                b.add(seppen)
        # print(b)
        #print('cost:' + str(cost))
        ans = min(ans, cost)
print(ans)
