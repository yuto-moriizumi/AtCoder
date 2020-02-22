import math
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
color = [-1]*n
edge = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

flag = True


def dfs(i, pre, c):
    if color[i] == c:
        return
    elif color[i] == 1-c:
        global flag
        flag = False
        return
    color[i] = c
    for v in edge[i]:
        dfs(v, i, 1-c)


dfs(0, -1, 0)
# print(color)
# print(flag)

if flag:
    print(color.count(1)*color.count(0)-m)
else:
    print(math.floor(n*(n-1)/2-m))
