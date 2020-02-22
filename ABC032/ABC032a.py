# ABC032a
from fractions import gcd
from functools import reduce
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def lcm_base(a, b):
    return a * b // gcd(a, b)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


a = int(input())
b = int(input())
n = int(input())

j = lcm_base(a, b)
ans = lcm_base(a, b)
for i in range(1, 200000):
    if j*i >= n:
        print(j*i)
        exit(0)
