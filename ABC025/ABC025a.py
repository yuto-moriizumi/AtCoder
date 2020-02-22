# ABC025a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = sorted(list(input()[:-1]))
# print(s)
n = int(input())

print(s[(n-1)//5]+s[(n-1) % 5])
