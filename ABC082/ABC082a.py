# ABC082a
from math import ceil
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


a, b = map(int, input().split())
print(ceil((a+b)/2))
