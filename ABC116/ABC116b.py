# ABC116b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = int(input())


def f(n):
    if(n % 2 == 0):
        return n//2
    else:
        return 3*n+1


a = [0, s]

for i in range(2, 10**6):
    num = f(a[i-1])
    a.append(num)
    idx = a.index(num)
    #print(a)
    if(idx+1 < i):
        print(i)
        exit()
