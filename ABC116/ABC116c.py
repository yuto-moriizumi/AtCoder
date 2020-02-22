# ABC116c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
h = list(map(int, input().split()))

ans = 0
mode = 0

for i in h:
    while i > mode:
        mode += 1
        ans += 1
    while i < mode:
        mode -= 1
print(ans)
