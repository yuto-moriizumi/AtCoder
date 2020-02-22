# ABC101a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = list(input()[:-1])
print(s.count('+')-s.count('-'))
