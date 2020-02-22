# ABC074b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0

for i in x:
    ans += min(i, abs(k-i))

print(ans*2)
