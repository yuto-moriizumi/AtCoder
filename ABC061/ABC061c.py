# ABC061c
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
nums.sort()
i = 0
for a, b in nums:
    i += b
    if i >= k:
        print(a)
        exit(0)
