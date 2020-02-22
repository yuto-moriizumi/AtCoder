#ABC056b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

w, a, b = map(int, input().split())
if (a + w < b):
    print(b - (a + w))
elif (b + w < a):
    print(a - (b + w))
else:
    print(0)
exit(0)

if (abs(a - b) <= w):
    print(0)
else:
    print(abs(a - b) - w)
