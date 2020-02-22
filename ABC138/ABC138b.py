# ABC138b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

input()
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += 1/i
print(1/ans)
