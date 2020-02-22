# ABC141b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]

even = set()
odd = set()

for i in range(0, len(s), 2):
    even.add(s[i])
for i in range(1, len(s), 2):
    odd.add(s[i])
#print(odd, even)
print('Yes' if (len(odd - set(list('LUD'))) == 0) and (
    len(even - set(list('RUD'))) == 0) else 'No')
