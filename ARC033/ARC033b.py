na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

t = len(a & b)
t2 = len(a.union(b))
print(t/t2)
