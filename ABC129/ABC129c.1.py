import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = []
for _ in range(m):
    a.append(int(input()))

memo = {}


def step(now):
    if (memo.get(now) != None):
        return memo[now]
    if (now in a):
        return 0
    # print(now)
    if (now == 0):
        return 1
    if (now < 0):
        return 0
    #ssprint(now)
    memo[now] = step(now-1)+step(now-2)
    return memo[now]


print(step(n) % 1000000007)
# print(memo)
