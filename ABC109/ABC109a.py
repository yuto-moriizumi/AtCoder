# ABC109a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print('YNeos'[a*b % 2 == 0::2])
