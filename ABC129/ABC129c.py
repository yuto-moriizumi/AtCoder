import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = []
for _ in range(m):
    a.append(int(input()))
a=set(a)

memo = {}


def step(now):
    if now in a:
        return 0
    # print(now)
    if now == n:
        return 1
    if now > n:
        return 0
    if memo.get(now) != None:
        return memo[now]
    # print(now)
    memo[now] = step(now+1)+step(now+2)
    return memo[now]


print(step(0) % 1000000007)
print(memo)
