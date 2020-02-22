# ABC139b
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print(math.ceil((b-1) / (a-1)))
