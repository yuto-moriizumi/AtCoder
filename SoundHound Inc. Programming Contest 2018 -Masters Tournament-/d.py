import heapq
import collections
n, m, s, t = map(int, input().split())


class Edge:
    def __init__(self, to, yen, snuuk):
        self.to = to
        self.yen = yen
        self.snuuk = snuuk


edges = [list() for _ in range(n)]

for _ in range(m):
    u, v, a, b = map(int, input().split())
    edges[u-1].append(Edge(v-1, a, b))
    edges[v-1].append(Edge(u-1, a, b))

dist = [10**10]*n

heap = []
heapq.heapify(heap)
# heapq.heappush()

q = collections.deque()
q.append((s-1, 0))

while(len(q) != 0):
    v, cost = q.popleft()
    if dist[v] <= cost:
        continue
    dist[v] = cost
    for i in edges[v]:
        q.append((i.to, cost+i.yen))

q2 = collections.deque()
q2.append((t-1, 0))
dist2 = [10**10]*n

while(len(q2) != 0):
    v, cost = q2.popleft()
    if dist2[v] <= cost:
        continue
    dist2[v] = cost
    for i in edges[v]:
        q2.append((i.to, cost+i.snuuk))

# print(dist)
# print(dist2)
ans = [0]*n

ans[n-1] = 10**15-dist[n-1]-dist2[n-1]
for i in range(n-2, -1, -1):
    ans[i] = max(10**15-dist[i]-dist2[i], ans[i+1])

for i in range(n):
    print(ans[i])
