# ABC060a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = input().split()
print('YNEOS'[a[-1] != b[0] or b[-1] != c[0]::2])
