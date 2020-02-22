#Union-Find木
import sys
input = sys.stdin.readline

n,q=map(int,input().split())
tree=[]
for i in range(n):
    tree.append(i)

def root(x):
    if(tree[x]==x):
        return x
    tree[x]=root(tree[x])
    return tree[x] #経路圧縮

def same(x,y): #xとyが同じ木に属するか
    return root(x)==root(y)


def unite(x,y):
    x=root(x)
    y=root(y)
    if(x==y):
        return
    tree[x]=y

for _ in range(q):
    p,a,b=map(int,input().split())
    if(p==0):
        unite(a,b)
        continue
    if(same(a,b)):
        print("Yes")
        continue
    print("No")
    