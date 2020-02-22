# ABC076c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

ss = list(input())[:-1]
t = list(input())[:-1]

pos = len(ss)-len(t)
while (pos > 0):
    #print(ss[pos:pos+len(t)], t, pos)
    for i in range(len(t)):
        if (ss[pos + i] != '?' and ss[pos + i] != t[i]):
            pos -= 1
            break
        if (i == len(t) - 1):
            for j in range(len(t)):
                ss[pos+j] = t[j]
            pos = -1
if (pos != -1):
    print('UNRESTORABLE')
    exit()
# print('hi')
# print(ss)

for i in range(len(ss)):
    if (ss[i] == '?'):
        ss[i] = 'a'
print(*ss, sep='')
