# ABC060b
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c = map(int, input().split())

for i in range(a, a * b+a, a):
    if (i % b == c):
        #print(i, b, i % b, c)
        print('YES')
        exit()
print('NO')
