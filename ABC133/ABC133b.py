# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)


def kyori(l1, l2):
    goukei = 0
    for i in range(len(l1)):
        goukei += (l1[i] - l2[i]) ** 2
    return goukei**0.5


n, d = map(int, input().split())
x = []
for _ in range(n):
    x.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if (kyori(x[i], x[j]).is_integer()):
            #print(i, j, kyori(x[i], x[j]).is_integer())
            ans += 1
print(ans)
