# ABC102a
from fractions import gcd
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())


def lcm_base(a, b):
    return a * b // gcd(a, b)


print(lcm_base(n, 2))
