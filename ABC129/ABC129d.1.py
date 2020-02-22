import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

L = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if(s[i][j]=="#"):
            L[i][j]=0
            continue
        if(j==0):
            L[i][j]=1
            continue
        L[i][j]=L[i][j-1]+1

S = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h):
        if(s[i][j]=="#"):
            S[i][j]=0
            continue
        if(i==0):
            S[i][j]=1
            continue
        S[i][j]=S[i-1][j]+1

W = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w-1,0,-1):
        if(s[i][j]=="#"):
            W[i][j]=0
            continue
        if(j==w-1):
            W[i][j]=1
            continue
        W[i][j]=W[i][j+1]+1

N = [[0]*w for _ in range(h)]
for j in range(w):
    for i in range(h-1,0,-1):
        if(s[i][j]=="#"):
            N[i][j]=0
            continue
        if(i==h-1):
            N[i][j]=1
            continue
        N[i][j]=N[i+1][j]+1

result=0
for i in range(h):
    for j in range(w):
        result=max(result,L[i][j]+S[i][j]+W[i][j]+N[i][j]-3)

print(result)