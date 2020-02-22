# ABC134b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, d = map(int, input().split())
if(n % (d * 2 + 1) != 0):
    print(n // (d * 2 + 1) + 1)
    exit()
print(n // (d * 2 + 1))
