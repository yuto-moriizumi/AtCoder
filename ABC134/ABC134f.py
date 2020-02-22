# ABC134f
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(i+1)

memo = {}


def keisan(a, i, kk):
    if (len(a) == 0):
        if (kk == k):
            return 1
        return 0
    if (memo.get((a, i, kk))):
        return memo[(a, i, kk)]
    count = 0
    for j in a:
        ta = copy.copy(a)
        ta.remove(j)
        count += keisan(ta, i + 1, kk + abs(i - j))
    memo[(a, i, kk)] = count
    return count


print(keisan(a, 1, 0))
