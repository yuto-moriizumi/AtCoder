# ABC104a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r = int(input())
if r < 1200:
    print('ABC')
    exit(0)
if r < 2800:
    print('ARC')
    exit(0)
print('AGC')
