#ABC143a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print(max(0, a-b*2))