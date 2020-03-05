# ABC041d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    N, M = map(int, input().split())
    edge = [0]*N
    for i in range(M):
        x, y = map(int, input().split())
        edge[x-1] |= 1 << (y-1)
    dp = [0]*(1 << N)
    dp[0] = 1
    for s in range(1, 1 << N):  # 集合を添字の小さい順に試す
        for i in range(N):  # 全ての要素を考える
            # i in sかつedge[i]とsが共通部分を持たない
            if ((s >> i) & 1) and (not(edge[i] & s)):
                dp[s] += dp[s ^ (1 << i)]
    return dp[-1]


print(main())
