# ABC065a
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, a, b = map(int, input().split())
if a-b < -x:
    print('dangerous')
elif b > a:
    print('safe')
else:
    print('delicious')
