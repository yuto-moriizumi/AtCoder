from collections import Counter
s = input()
l = len(s)

for i in Counter(s).most_common():
    largest = i[1]
    if largest == 1:
        print('YES')
        exit(0)
    if l >= largest * 2:
        l -= 1
        continue
    print('NO')
    exit(0)
print('YES')
