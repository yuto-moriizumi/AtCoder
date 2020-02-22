# ABC073a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = list(input())
print('YNeos'[not '9' in n::2])
