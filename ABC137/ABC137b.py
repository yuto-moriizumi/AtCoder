# ABC137b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

k, x = map(int, input().split())
for i in range(x - k+1, x + k-1):
    print(i, end=" ")
print(x+k-1)
