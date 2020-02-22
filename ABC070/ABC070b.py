# ABC070b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, d = map(int, input().split())
print(max(0, min(b, d)-max(a, c)))
