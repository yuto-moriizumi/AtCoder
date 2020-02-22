import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cost = 0
if (a >= 13):
    print(b)
elif (a >= 6):
    print(b // 2)
else:
    print(0)
