import sys
input = sys.stdin.readline

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

count = 0
for j in range(N):
    t = 0
    for i in range(M):
        t += A[j][i]*B[i]
    t += C
    if(t > 0):
        count += 1

print(count)
