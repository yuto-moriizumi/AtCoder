# ABC104b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
#print(s.count('C', 2, -1))
if (s[0] != 'A' or s.count('C', 2, -1) != 1):
    print('WA')
    # print('hi')
    exit()
cPos = s.find('C', 2, -1)
if (s[1:cPos].islower() and s[cPos + 1:].islower()):
    # print('hi')
    print('AC')
    exit()
print('WA')
