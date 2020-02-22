# ABC022b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = [int(input()) for _ in range(n)]
visited = set()
ans = 0
for i in a:
    if i in visited:
        ans += 1
    visited.add(i)
print(ans)
