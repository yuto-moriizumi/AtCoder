import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
kakuritu = 0

for saikoro in range(1, n + 1):
    if(saikoro < k):
        kaisu = math.ceil(math.log2(k / saikoro))
        kakuritu += 2 ** (-1 * kaisu)
    else:
        kakuritu += 1

print(kakuritu/n)
