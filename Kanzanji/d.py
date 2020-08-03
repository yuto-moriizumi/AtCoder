n, k = map(int, input().split())
p = list(map(int, input().split()))
maxI = 0
maxT = 0
t = 0
for i in range(n):
    t += p[i]
    if k <= i:
        t -= p[i-k]
    if maxT < t:
        maxT = t
        maxI = i
ans = 0


def calc(n):
    return n*(n+1)/2/n
    ans = 0
    for i in range(1, n+1):
        ans += i/n
    return ans


for i in range(maxI-k+1, maxI+1):
    #print(i, p[i])
    ans += calc(p[i])
# print(p)
#print(maxT, maxI)
print(ans)
