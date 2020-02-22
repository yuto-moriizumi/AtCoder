# ABC044a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
k = int(input())
x = int(input())
y = int(input())

print(k*x+(n-k)*y if n >= k else n*x)
