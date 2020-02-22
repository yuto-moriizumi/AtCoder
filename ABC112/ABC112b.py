# ABC112b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, t = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

ans = 9999

for i in c:
    if (i[1] <= t):
        ans = min(ans, i[0])
print(ans if ans != 9999 else 'TLE')
