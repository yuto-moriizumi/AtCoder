n = int(input())
d = []
for i in range(n):
    d.append(int(input()))

c = 0
lastSize = 0
while(True):
    if(len(d) != 0):
        np = max(d)
        d.remove(np)
        if(np != lastSize):
            lastSize = np
            c += 1
    else:
        break
print(c)
