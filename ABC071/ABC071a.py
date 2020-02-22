# ABC071a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, a, b = map(int, input().split())
print('AB'[abs(x-a) > abs(x-b)::2])
