# 最初に入れておくとinputが早くなる
import sys
import numpy as np
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
ans = [0]*n

for i in range(0, a[0]*2+1, 2):
    ans[0] = i
    tempa = [0]*n
    for j in range(n):
        tempa[j] = ans[j % n] // 2
        if(j+1 != n):
            ans[(j + 1) % n] = (a[j] - tempa[j]) * 2
    print(a, tempa, ans)
    if (ans[0] == (a[n - 1] - tempa[n - 1]) * 2):
        break
# tempa[1 % 3] = ans[1 % 3]/2
# ans[2 % 3] = (a[1]-tempa[1])*2
# tempa[2 % 3] = ans[2 % 3]/2
# ans[3 % 3] = (a[2 % 3]-tempa[2 % 3])*2
# tempa[3 % 3] = ans[3 % 3] / 2
# print(a)
# print(tempa)
print(*ans)
