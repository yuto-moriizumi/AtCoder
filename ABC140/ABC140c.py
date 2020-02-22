# ABC140c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
b = list(map(int, input().split()))
a = [0]*n

a[0] = b[0]
for i in range(n - 1):
    a[i] = min(a[i], b[i])
    a[i+1] = b[i]
    # print(a)
print(sum(a))
