#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

#幅優先探索 探索済みを数字に置換する

r,c=map(int,input().split())
sy,sx=[int(i)-1 for i in input().split()]
gy,gx=[int(i)-1 for i in input().split()]
c=[list(input()) for _ in range(r)]

q=[]
dxy=((1,0),(-1,0),(0,1),(0,-1))

q.append((sx,sy));
c[sy][sx]="0"

for x,y in q:
    for dx,dy in dxy:
        if c[y+dy][x+dx]==".":
            q.append((x+dx,y+dy))
            c[y+dy][x+dx]=int(c[y][x])+1

print(c[gy][gx])