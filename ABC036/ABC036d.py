# ABC036d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
bridge = [list() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    bridge[a-1].append(b-1)
    bridge[b-1].append(a-1)
# dfs(i,color)=島i番目をcolorで塗った時の塗り方の総数

# print(bridge)
W = [0]*n
B = [0]*n
mod = 10**9+7


def dfs(i, pre):
    W[i] = B[i] = 1
    for j in bridge[i]:
        if pre == j:
            continue
        dfs(j, i)
        W[i] = W[i] * (W[j]+B[j]) % mod
        B[i] = B[i]*W[j] % mod


dfs(0, -1)
print((W[0]+B[0]) % mod)
