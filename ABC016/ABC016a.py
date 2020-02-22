# ABC016a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, d = map(int, input().split())
print('YNEOS'[m % d != 0::2])
