# ABC103c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
ans = 0
f = 0
for j in a:
    f += j-1
#print(f, m)
ans = max(ans, f)
print(ans)
