# ABC079c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = input()[:-1]


def dfs(pos, formula):
    if (pos > 3):
        # print(formula)
        return formula if eval(formula) == 7 else False
    #print(pos, n[pos])
    f = dfs(pos + 1, formula + '+'+n[pos])
    if (not f):
        return dfs(pos + 1, formula + '-'+n[pos])
    else:
        return f


print(dfs(1, n[0])+'=7')
