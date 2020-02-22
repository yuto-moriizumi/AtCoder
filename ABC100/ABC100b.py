# ABC100b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

d, n = map(int, input().split())
print(100**d*(n if n != 100 else 101))
