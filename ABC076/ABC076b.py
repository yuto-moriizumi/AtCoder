# ABC076b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())

ans = 10**4

for i in range(n+1):
    ans = min(ans, 2**i+k*(n-i))

print(ans)
