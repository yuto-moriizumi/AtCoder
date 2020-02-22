n=int(input())
t=[0]
x=[0]
y=[0]
for i in range(n):
    tt,tx,ty=map(int,input().split())
    t.append(tt)
    x.append(tx)
    y.append(ty)

isAvailabe= True
for i in range(1,n+1):
    mitinori=abs(x[i]-x[i-1])+abs(y[i]-y[i-1])
    if(t[i]-t[i-1]>=mitinori):
        if((t[i]-t[i-1]-mitinori)%2==1):
            isAvailabe=False
    else:
        isAvailabe=False

if(isAvailabe):
    print("Yes")
else:
    print("No")