# ABC068b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

ans = 0
for i in range(8):
    if n >= 2 ** i:
        ans = i
print(2**ans)
