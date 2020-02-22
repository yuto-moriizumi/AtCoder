import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = []
for _ in range(m):
    k.append(list(map(int, input().split())))
p = list(map(int, input().split()))

denkyu = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
memo = []
memos = []


def erabu(i, n, c, d):
    if (i > len(k[d][1:])):
        if(c % 2 == p[d]):
            memo.append(n)
        return
    if(i+1 in k[d][1:]):
        erabu(i+1, n.append(i+1), c+1, d)
    erabu(i + 1, n, c, d)


print(memo)

for i in range(m):
    erabu(0, 0, 0, i)
    memos.append(memo)

# for i in range(len(memos[0])):

# def isOK(i, n):
 #   if (n ^ memos[i][j] not 0)
