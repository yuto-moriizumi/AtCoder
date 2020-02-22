# ABC070a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = input()[:-1]
print('YNeos'[n != n[::-1]::2])
