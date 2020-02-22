# ABC040a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, x = map(int, input().split())
print(min(x-1, n-x))
