l,x,y,s,d=map(int,input().split())

tokei=d-s
if tokei<0:
    tokei+=l
han=l-d+s
if s>d:
    han-=l

ans=tokei/(y+x) if y+x!=0 else 10**12
ans=min(ans,han/(y-x) if y-x>0 else 10**12)
print(ans)