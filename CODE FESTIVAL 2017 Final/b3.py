from collections import Counter
s = input()
l = len(s)

a = s.count('a')
b = s.count('b')
c = s.count('c')

if max([a, b, c]) - min([a, b, c]) <= 1:
    print('YES')
    exit(0)
print('NO')
