# ABC038d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
box = [list(map(int, input().split())) for _ in range(n)]
box.sort()
# print(box)


def comp(box1, box2):
    if (box1[0] < box2[0]):
        if (box1[1] < box2[1]):
            return 1
        elif (box1[1] == box2[1]):
            return 1
        else:
            return 0
    elif (box1[0] == box2[0]):
        if (box1[1] < box2[1]):
            return 1
        elif (box1[1] == box2[1]):
            return 1
        else:
            return - 1
    else:
        if (box1[1] < box2[1]):
            return 0
        elif (box1[1] == box2[1]):
            return -1
        else:
            return - 1


# dp[i]=i番目の箱を使った時の最大の箱の数
dp = [1]*n
# print(dp)
for i in range(n):
    for j in range(i):
        if(box[j][0] < box[i][0] and box[j][1] < box[i][1]):
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
