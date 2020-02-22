# ABC024a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, k = map(int, input().split())
s, t = map(int, input().split())
print(s*a+t*b if s+t < k else s*a+t*b-c*(s+t))
