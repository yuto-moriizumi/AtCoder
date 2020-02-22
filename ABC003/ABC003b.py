# ABC003b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()
t = input()
a = list('atcoder')

for i in range(len(s)):
    if(s[i] != t[i] and (s[i] == '@' or t[i] == '@')):
        #print(s[i], t[i])
        if(s[i] in a or t[i] in a):
            continue
        else:
            print('You will lose')
            exit()
    if(s[i] == t[i]):
        continue
    else:
        print('You will lose')
        exit()
print('You can win')
