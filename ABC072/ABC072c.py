# ABC072c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
print((1900*m+100*(n-m))*2**m)
