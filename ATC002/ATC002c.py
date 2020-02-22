# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)

n = int(input())
w = list(map(int, input().split()))

# c1,2=3
# c1,2= min((c1,1+c2,2))+3=min(0)+3=3
# c2,3=5
# c1,3=min((c1,1+c2,3),(c1,2+c3,3))+6=min((0+5),(3+0))+6=min(5,3)+6=9
# 1*2+2*2+3*1=2+4+3=9
# c3,4=7
# c1,4=min(c1,2+c)

# 最適二分探索木
# DPです

dp = {}
ruisekiwa = [0]*(n+1)
for i in range(1, n+1):
    ruisekiwa[i] = ruisekiwa[i-1]+w[i-1]
# print(ruisekiwa)


def calcCost(i, j):
    if(i == j):
        return 0
    if(dp.get((i, j)) != None):
        return dp[(i, j)]
    cost = 10**10
    for k in range(i, j):
        cost = min(cost, calcCost(i, k)+calcCost(k+1, j))
    cost += ruisekiwa[j+1]-ruisekiwa[i]
    dp[(i, j)] = cost
    return cost


print(calcCost(0, n-1))
