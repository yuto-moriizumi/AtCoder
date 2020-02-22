import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
a = []
for _ in range(m):
    a.append(int(input()))
a=set(a)

memo = [0]*(n+1)
memo[0]=1
if not(1 in a):
    memo[1]=1

for i in range(2,n+1):
    #print(i)
    if i in a:
        continue
    #print(memo[i-1],memo[i-2])
    memo[i]=memo[i-2]+memo[i-1]
            

#print(memo)
print(memo[n]% 1000000007)
