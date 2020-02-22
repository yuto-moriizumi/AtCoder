# ABC072a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, t = map(int, input().split())

print(max(x-t, 0))
