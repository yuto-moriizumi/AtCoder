# ABC115b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p = [int(input()) for _ in range(n)]
print(sum(p)-max(p)//2)
