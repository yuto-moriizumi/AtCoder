import sys
input = sys.stdin.readline
x, y, z, k = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)            

abc=[]

for i in range(x):
    for j in range(y):
        for l in range(z):
                if((i+1)*(j+1)*(l+1)<=k):
                        abc.append(a[i]+b[j]+c[l])

abc.sort(reverse=True)
for i in abc[:k]:
    print(i)