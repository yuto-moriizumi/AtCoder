# ABC083a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

a, b, c, d = map(int, input().split())
if a+b < c+d:
    print('Right')
elif a+b == c+d:
    print('Balanced')
else:
    print('Left')
