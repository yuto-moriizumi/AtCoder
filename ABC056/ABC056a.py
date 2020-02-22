# ABC056a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, d = input()[:-1].split()
print('DH'[a == d])
