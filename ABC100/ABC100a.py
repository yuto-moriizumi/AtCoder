# ABC100a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print('Yay!' if max(a, b) <= 8 else ':(')
