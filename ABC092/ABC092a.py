# ABC092a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b)+min(c, d))
