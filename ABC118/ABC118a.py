# ABC118a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())
print(a+b if b % a == 0 else b-a)
