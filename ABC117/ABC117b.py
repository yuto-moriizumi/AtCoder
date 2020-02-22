# ABC117b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

input()
l = list(map(int, input().split()))
print('Yes' if max(l) < sum(l)-max(l) else 'No')
