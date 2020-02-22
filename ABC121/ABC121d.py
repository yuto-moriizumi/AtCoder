import sys
input = sys.stdin.readline

a, b = map(int, input().split())
v = 0
for j in range(len(bin(b))):
    c = 0
    for i in range(len(bin(b))-len(bin(a))):
        if(j-1 > len(bin(a+i))):
            t = bin(a+i)[-len(bin(a+i))]
        else:
            t = bin(a+i)[-j-1]
        if(t == "b"):
            c += 0
        else:
            c += int(t)
    if(c % 2 == 0):
        v += 2**j
print(v)
