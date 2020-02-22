# ABC037a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
print(c//min(a, b))
