# ABC017a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

pro = [tuple(map(int, input().split())) for _ in range(3)]
ans = 0
for s, e in pro:
    ans += s*e//10
print(ans)
