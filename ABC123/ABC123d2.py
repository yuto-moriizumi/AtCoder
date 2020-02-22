import sys
input = sys.stdin.readline

x, y, z, k = map(int, input().split())
a = sorted(int(i) for i in input().split())
b = sorted(int(i) for i in input().split())
c = sorted(int(i) for i in input().split())

#a.sort(reverse=True)
#b.sort(reverse=True)
#c.sort(reverse=True)

ab = sorted(i+j for i in a for j in b)[:-k-1:-1]
abc = sorted(i+j for i in ab for j in c)[:-k-1:-1]

print(*abc[:k], sep="\n")