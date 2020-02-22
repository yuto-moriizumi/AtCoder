# ABC030a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, d = map(int, input().split())
if b/a > d/c:
    print('TAKAHASHI')
elif b/a == d/c:
    print('DRAW')
else:
    print('AOKI')
