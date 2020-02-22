# ABC091a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
print('YNeos'[a+b < c::2])
