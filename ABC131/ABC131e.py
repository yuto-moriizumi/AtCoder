# 最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

fibo = [0 for _ in range(n)]
fibo[2] = 1

for i in range(3, n):
    fibo[i] = fibo[i-1]+fibo[i-2]*2+1

print(fibo)
