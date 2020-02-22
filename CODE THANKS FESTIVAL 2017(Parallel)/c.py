import heapq

n, k = map(int, input().split())
hq = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(hq, (a, b))
# print(hq)
ans = 0
for _ in range(k):
    time = heapq.heappop(hq)
    ans += time[0]
    heapq.heappush(hq, (time[0]+time[1], time[1]))
print(ans)
