n = int(input())
s = input()
t = input()

pos = 0

flag = True
for pos in range(n+1):
    flag = True
    for i in range(n-pos):
        if s[i+pos] != t[i]:
            flag = False
    if flag:
        print(n+pos)
        exit(0)
print(2*n)
