n, a, b = map(int, input().split())
oknum = 0
number = []
for n in range(n):
    if(a <= sum([int(i) for i in list(str(n+1))]) <= b):
        oknum += n+1
print(oknum)
