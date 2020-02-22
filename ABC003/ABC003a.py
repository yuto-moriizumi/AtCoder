# ABC003a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += 10000*i
print(ans//n)
