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
for i in range(n):
    if(x[i]+y[i]>t[i] or (x[i]+y[i]+t[i])%2!=0:
        print("NO")

print("YES")