# ABC118c
from functools import reduce
from fractions import gcd
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))


def gcds(*numbers):
    return reduce(gcd, numbers)


print(gcds(a))
exit(0)


def solve(l):
    m = min(l)
    nl = list()
    for i in l:
        if i % m != 0:
            nl.append(i % m)
    nl.append(m)
    # print(nl)
    if len(nl) == 1:
        return m
    return solve(nl)


print(solve(a))
