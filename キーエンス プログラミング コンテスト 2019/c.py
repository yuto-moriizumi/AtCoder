import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n):
    c.append(b[i]-a[i])
#print(c)
ans = 0
su = 0
for i in c:
    if (i > 0):
        ans += 1
        su += i
#print(ans, su)
heapq.heapify(c)
#print(c)
while (su > 0):
    t = heapq.heappop(c)
    if (t >= 0):
        print(-1)
        exit(0)
    su += t
    ans += 1
print(ans)
