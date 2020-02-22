# ABC052a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, d = map(int, input().split())
print(max(a*b, c*d))
