# ABC061b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

ans = [0] * n

for r in a:
    ans[r[0]-1] += 1
    ans[r[1]-1] += 1

for a in ans:
    print(a)
