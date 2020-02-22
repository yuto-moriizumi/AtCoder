# ABC105a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
print(0 if n % k == 0 else 1)
