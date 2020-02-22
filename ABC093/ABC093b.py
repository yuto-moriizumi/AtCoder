# ABC093b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, k = map(int, input().split())

for i in range(a, min(a + k, b+1)):
    print(i)
# print('hi')
for i in range(max(b - k+1, a+k), b + 1):
    print(i)
