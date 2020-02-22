# ABC080a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())
print(min(a*n, b))
