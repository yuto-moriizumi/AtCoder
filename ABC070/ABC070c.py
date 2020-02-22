# ABC070c
from fractions import gcd
from functools import reduce
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())


def lcm_base(a, b):
    return a * b // gcd(a, b)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def gcds(*numbers):
    return reduce(gcd, numbers)


t = [int(input()) for _ in range(n)]
print(lcm(*t))
