#深さ優先探索
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

H,W=map(int,input().split())
c=[]
memo=[]
startX=startY=0

for j in range(H):
    memo.append([])
    l=input()
    for i in range(len(l)):
        memo[j].append(False)
        if(l[i]=="s"):
            #print(True)
            startX=i
            startY=j
    c.append(l)

#print(startX,startY)

def search(x,y):
    if x<0 or W<=x or y<0 or H<=y or c[y][x]=="#" or memo[y][x]:
        return False
    memo[y][x]=True
    if c[y][x]=="g":
        return True
    return search(x+1,y) or search(x,y+1) or search(x-1,y) or search(x,y-1)

if(search(startX,startY)):
    print("Yes")
    exit()
print("No")