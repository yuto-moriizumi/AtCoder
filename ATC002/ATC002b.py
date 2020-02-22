#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline
#import numpy as np

n, m, p = map(int, input().split())
#print(n**p%m)
#print(np.mod(np.power(n,p),m))


def zijo(n, p):
    if (p <= 1):
        return n**p % m
    if (p % 2 == 0):
        return zijo(n, p // 2)**2 % m
    return zijo(n, p - 1) * n % m


print(zijo(n, p))
