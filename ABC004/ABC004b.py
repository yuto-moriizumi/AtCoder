# ABC004b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

grid = [list(input().split()) for _ in range(4)]

for i in range(3, -1, -1):
    print(*grid[i][::-1], sep=' ', end='')
    print()
