n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = dict()

if n == 1:
    print(1)
    exit()

for i in range(n):
    for j in range(n):
        if (i == j):
            continue
        p = xy[j][0] - xy[i][0]
        q = xy[j][1] - xy[i][1]
        if ans.get((p, q)) == None:
            ans[(p, q)] = 1
        else:
            ans[(p, q)] += 1
# print(ans)
print(n-max(ans.values()))
