# ABC058a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())
print('YNEOS'[b-a != c-b::2])
