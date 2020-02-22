# ABC105b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

for i in range(0, n+1, 4):
    if ((n - i) % 7 == 0):
        print('Yes')
        exit()
print('No')
