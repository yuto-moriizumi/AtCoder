# ABC097a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, d = map(int, input().split())
print('YNeos'[not(abs(a-c) <= d or abs(a-b) <= d and abs(b-c) <= d)::2])
