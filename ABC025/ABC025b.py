# ABC025b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())
order = [tuple(input().split()) for _ in range(n)]
pos = 0
for i in order:
    s, t = i
    t = int(t)
    if s == 'East':
        pos += min(b, max(a, t))
    else:
        pos -= min(b, max(a, t))
if pos > 0:
    print('East', pos)
elif pos == 0:
    print(0)
else:
    print('West', -pos)
