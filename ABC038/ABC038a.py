# ABC038a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
print('YNEOS'[s[-1] != 'T'::2])
