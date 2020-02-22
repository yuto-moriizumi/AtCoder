# ABC094b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = 0
for i in a:
    if (i > x):
        left += 1
    else:
        right += 1
print(min(left, right))
