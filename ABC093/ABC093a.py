# ABC093a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = list(input()[:-1])
s.sort()
print('YNeos'[s != list('abc')::2])
