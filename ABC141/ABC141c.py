# ABC141c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

sanka = [0]*n

for i in a:
    sanka[i-1] += 1
# print(sanka)

for i in sanka:
    print('Yes' if i+k-q > 0 else 'No')
