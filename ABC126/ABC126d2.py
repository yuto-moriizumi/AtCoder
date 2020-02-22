# Union-Find木
import sys
input = sys.stdin.readline

n = int(input())
tree = [0]
for i in range(1, n+1):
    tree.append(i)


def root(x):
    if(tree[x] == x):
        return x
    tree[x] = root(tree[x])
    return tree[x]  # 経路圧縮


def same(x, y):  # xとyが同じ木に属するか
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    if(x == y):
        return
    tree[x] = y


for _ in range(n-1):
    u, v, w = map(int, input().split())
    if(w % 2 == 0):
        unite(u, v)

for i in range(1, n+1):
    if (same(1, i)):
        print(0)
    else:
        print(1)
