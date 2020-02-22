# ABC098a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print(max(a+b, a-b, a*b))
