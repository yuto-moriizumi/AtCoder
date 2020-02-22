# ABC023a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input()[:-1]
ans = 0
for i in n:
    ans += int(i)
print(ans)
