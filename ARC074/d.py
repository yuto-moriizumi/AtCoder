import heapq
n = int(input())
a = list(map(int, input().split()))

ans = 1-10**10
for i in range(n, 2*n+1):
    ll = a[:i]
    heapq.heapify(ll)
    for j in range(i-n):
        heapq.heappop(ll)
    rl = a[i:]
    heapq.heapify(rl)
    rsum = sum([heapq.heappop(rl) for _ in range(n)])
    ans = max(ans, sum(ll)-rsum)
    #print(ll, rsum, sum(ll)-rsum)
print(ans)
