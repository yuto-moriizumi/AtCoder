# ABC099b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
left = sum(range(1, b - a))
print(left-a)
