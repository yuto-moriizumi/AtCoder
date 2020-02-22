import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

k, n = map(int, input().split())
memo = dict()


def fibo(i):
    if i <= k:
        return 1
    if memo.get(i) == None:
        memo[i] = sum([fibo(i-j) for j in range(1, k+1)])
    return memo[i]


print(fibo(n))
