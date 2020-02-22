# ABC015a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = input()[:-1]
b = input()[:-1]
print(a if len(a) > len(b) else b)
