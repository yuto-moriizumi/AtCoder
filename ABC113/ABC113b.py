# ABC113b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if(abs(a-(t-h[i]*0.006)) <= abs(a-(t-h[ans]*0.006))):
        #print(abs(a-(t-h[i]*0.006)), score)
        ans = i
print(ans+1)
