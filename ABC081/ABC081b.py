input()
n = list(map(int, input().split()))
c = 0
odd = False
while(True):
    for i in n:
        if(i % 2 != 0):
            odd = True
    if(odd == False):
        n = [i/2 for i in n]
        c += 1
        continue
    break
print(c)
