n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
num = []
for i in a:
    for j in b:
        num.append(i*j)
num.sort()
print(num[k-1])
