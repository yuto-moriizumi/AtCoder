#ABC042a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = list(map(int, input().split()))
print("YES" if n.count(5) == 2 and n.count(7) == 1 else "NO")
