# ABC143d
import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
l = list(map(int, input().split()))

ans = 0

l.sort()
# print(l)
for x in range(n):
    for y in range(x+1, n):
        t = bisect.bisect_left(l, max(l[x] - l[y], l[y] - l[x])+1, y+1)
        #print(l[x], l[y], max(l[x] - l[y], l[y] - l[x]), t, l[t])
        t2 = bisect.bisect_left(l, l[x] + l[y], y+1)
        #print(t2, l[t2] if t2 < n else None)
        #print(t2 - t)
        t3 = t2 - t
        if t3 > 0:
            ans += t3
print(ans)
