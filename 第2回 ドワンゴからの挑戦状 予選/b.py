n=int(input())
k=list(map(int,input().split()))
ans=[k[0]]
for i in range(n-2):
    ans.append(min(k[i],k[i+1]))
ans.append(k[-1])
print(*ans)