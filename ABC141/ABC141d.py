# ABC141d
import sys
import heapq
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = list(map(int, input().split()))

ha = []

for i in a:
    heapq.heappush(ha, -i)


# print(ha)

for _ in range(m):
    heapq.heappush(ha, math.ceil(heapq.heappop(ha)/2))

# print(ha)
print(-sum(ha))
