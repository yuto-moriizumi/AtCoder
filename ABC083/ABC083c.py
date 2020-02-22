# ABC083c
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, y = map(int, input().split())

#y - x * 2 ** n > 0
#x * 2 ** n < y
# 2**n<y/x

# print(math.floor(math.log2(y/x))+1)
ans = 0
while (x <= y):
    ans += 1
    x *= 2
print(ans)
