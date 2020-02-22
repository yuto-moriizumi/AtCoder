# ABC138a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a = int(input())
s = input()[:-1]
print(s if a >= 3200 else 'red')
