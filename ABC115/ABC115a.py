# ABC115a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

d = int(input())
print('Christmas', end='')
if d < 25:
    print(' Eve', end='')
if d < 24:
    print(' Eve', end='')
if d < 23:
    print(' Eve', end='')
