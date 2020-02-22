# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)

L, R = map(int, input().split())

ans = 2018

for i in range(L, min(L+2020, R+1)):
    for j in range(i+1, min(L + 2020, R+1)):
        #print(i, j, (i % 2019) * (j % 2019) % 2019)
        ans = min(ans, (i % 2019) * (j % 2019) % 2019)
print(ans)
