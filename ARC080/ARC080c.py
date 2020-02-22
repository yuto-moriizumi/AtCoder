n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] % 4 == 0:
        a[i] = 2
    elif a[i] % 2 == 0:
        a[i] = 1
    else:
        a[i] = 0
# print(a)
if a.count(1) == 1:
    if a.count(0) <= a.count(2):
        print('Yes')
        exit(0)
    print('No')
    exit(0)
if a.count(2) > 0 and a.count(0) <= a.count(2)+1:
    print('Yes')
    exit(0)
if a.count(0) == 0:
    print('Yes')
    exit(0)
print('No')
