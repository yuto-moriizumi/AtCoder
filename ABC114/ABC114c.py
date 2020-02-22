# ABC114c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
okForm = set((3, 5, 7))
memo = dict()


def create(cn, nn):
    if memo.get((cn, nn)) != None:
        return memo[(cn, nn)]
    num = int(str(nn)+str(cn))
    if (num > n):
        return 0
    ans = 1 if set(map(int, list(str(num)))) == okForm else 0
    #print(num, cn, nn)
    ans += create(num, 3) + create(num, 5) + create(num, 7)
    memo[(cn, nn)] = ans
    return ans


print(create('', 3)+create('', 5)+create('', 7))
