# ABC016c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
edges = [list() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b-1].append(a-1)


def calc1(i):
    return set(edges[i])


def calc2(i):
    t = set()
    for j in edges[i]:
        t = t.union(calc1(j))
    t.difference_update(calc1(i))
    if i in t:
        t.remove(i)
    return len(t)


for i in range(n):
    print(calc2(i))
