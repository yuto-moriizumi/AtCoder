# ABC055b
import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# ABC055a
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
print(math.factorial(n) % (10**9 + 7))
