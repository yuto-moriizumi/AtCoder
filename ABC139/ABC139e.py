# ABC139e
import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = [collections.deque(map(int, input().split())) for _ in range(n)]
pos = [0] * n

day = 0
# print(a)
while (True):
    l = set()
    for i in range(n):
        if (pos[i] < n-1):
            aite = a[i][pos[i]]-1
            if (a[aite][pos[aite]]-1 == i):
                l.add(i)
    if (len(l) == 0):
        break
    for i in l:
        pos[i] += 1
    # print(l)
    l.clear()
    day += 1
    # print(a)
if(max(pos) == n-1):
    print(day)
else:
    print(-1)
