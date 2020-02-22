# ABC031a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, d = map(int, input().split())

print(max((a+1)*d, a*(d+1)))
