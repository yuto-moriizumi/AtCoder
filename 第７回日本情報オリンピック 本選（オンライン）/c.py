import bisect
# a = [1, 2, 3, 4, 5, 7, 8, 9]
# b = [1, 5, 10, 315, 321651]

# print(bisect.bisect(b, 314))

# exit()
n, m = map(int, input().split())
p = [int(input()) for _ in range(n)]
p.append(0)
p.sort()
preans = set()

ans = 0
# print(p)
for i in p:
    if (i > m):
        break
    for j in p:
        #print(i, j)
        if (i + j > m):
            preans.add(i)
            break
        preans.add(i + j)
#
preans = list(preans)
preans.sort()
# print(preans)
# print('ha')
for i in preans:
    pos = bisect.bisect(preans, m-i)-1
    # if (pos == -1):
    #    ans = max(ans, i)
    #    break
    # else:
    ans = max(ans, i + preans[pos])
print(ans)
