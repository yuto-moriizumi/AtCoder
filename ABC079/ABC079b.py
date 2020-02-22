# ABC079b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

memo = {}


def getLuca(nu):
    if (nu == 0):
        return 2
    if (nu == 1):
        return 1
    if (memo.get(nu) != None):
        return memo[nu]
    memo[nu] = getLuca(nu-1)+getLuca(nu-2)
    return memo[nu]


print(getLuca(n))
