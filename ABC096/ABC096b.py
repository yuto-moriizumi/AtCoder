# ABC096b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = list(map(int, input().split()))
k = int(input())
print(sum(a)-max(a)+max(a)*2**k)
