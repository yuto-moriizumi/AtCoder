# ABC039c
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
ken = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si']
f = s.index('WW')
se = s.index('WW', f+1)
if se-f == 7:
    print(ken[4-f])
else:
    print(ken[len(ken)-f-1])
