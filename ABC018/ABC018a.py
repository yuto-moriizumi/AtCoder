# ABC018a
import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

q = []
heapq.heapify(q)
for i in range(1, 4):
    heapq.heappush(q, (-int(input()), i))
ans = [-1]*3

while(len(q) > 0):
    p, i = heapq.heappop(q)
    ans[i-1] = 3-len(q)

for i in ans:
    print(i)
