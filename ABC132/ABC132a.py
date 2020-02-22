# ABC132a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = list(input()[:-1])
s.sort()
print('YNeos'[s.count(s[0]) != 2 or s.count(s[2]) != 2::2])
