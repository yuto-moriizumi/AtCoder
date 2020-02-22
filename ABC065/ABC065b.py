# ABC065b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
a = [int(input()) for _ in range(n)]

count = 0
used = [False]*n


def push(i):
    # print('push'+str(i))
    global count
    count += 1
    if (i == 2):
        print(count)
        exit()
    if (used[i-1]):
        print('-1')
        exit()
    used[i-1] = True
    push(a[i-1])


push(a[0])
