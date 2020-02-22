# 最初に入れておくとinputが早くなる
import sys
import numpy as np
input = sys.stdin.readline

# スタック最大数をセット
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
b = 0
for i in range(1, n-1, 2):
    b += a[i]
ans[0] = sum(a)-2*b

tempa = [0]*n
for j in range(n):
    tempa[j] = ans[j % n] // 2
    if(j+1 != n):
        ans[(j + 1) % n] = (a[j] - tempa[j]) * 2
    #print(a, tempa, ans)
print(*ans)
