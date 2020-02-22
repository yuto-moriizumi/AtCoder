# ABC111b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
ans = 111

for i in range(1, 10):
    if (n <= 111 * i):
        ans = 111*i
        break
print(ans)
