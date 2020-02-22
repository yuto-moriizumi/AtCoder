# ABC141e
import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
kagi = []
for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    kagi.append([a, b, c, i, 2**i])

memo = dict()


def dfs(pos, used, unlock, used2):
    if (memo.get((pos, used2))):
        # print('memo')
        return memo[(pos, used2)]
    if (len(unlock) == 0):
        #cost = 0
        # for i in used:
        #    cost += kagi[i][0]
        # return cost
        return 0
    if (pos >= m):
        return 10 ** 10
    # print(pos, used, unlock, copy.deepcopy(used), set().add(pos))
    no = copy.deepcopy(used)
    no2 = copy.deepcopy(unlock)
    if (len(set(kagi[pos][2]).intersection(unlock)) == 0):
        memo[(pos, used2)] = dfs(pos+1, no, no2, used2)
        return memo[(pos, used2)]
    yes = copy.deepcopy(used)
    yes.add(pos)
    yes2 = copy.deepcopy(unlock)
    yes2 -= set([i for i in kagi[pos][2]])

    # print(yes, yes2)
    memo[(pos, used2)] = min(dfs(pos+1, yes, yes2, used2+kagi[pos][4]) +
                             kagi[pos][0], dfs(pos+1, no, no2, used2))
    return memo[(pos, used2)]


ans = dfs(0, set(), set([i for i in range(1, n+1)]), 0)
print(ans if ans != 10 ** 10 else -1)
