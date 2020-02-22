# ABC140d
import re
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
s = input()[:-1]
print(min(n-1, s.count('RL')+2*k-1))
