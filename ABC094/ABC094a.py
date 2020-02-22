# ABC094a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, x = map(int, input().split())
print('YNEOS'[not(0 <= x-a <= b)::2])
