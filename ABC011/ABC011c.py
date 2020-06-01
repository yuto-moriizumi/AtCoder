# ABC011c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
ng = [int(input()) for _ in range(3)]

cou = 0
if n in ng:
    print('NO')
    exit(0)
while n != 0:
    if cou >= 100:
        print('NO')
        exit(0)
    if n >= 3 and not n - 3 in ng:
        n -= 3
    elif n >= 2 and not n - 2 in ng:
        n -= 2
    elif n >= 1 and not n - 1 in ng:
        n -= 1
    else:
        print('NO')
        exit(0)
    cou += 1
print('YES')
