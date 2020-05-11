
n, l = map(int, input().split())
amida = [input() for _ in range(l)]
goal = input()

i = l-1
pos = goal.find('o')
while i >= 0:
    if pos > 0:
        if amida[i][pos - 1] == '-':
            i -= 1
            pos -= 2
            continue
    if pos < 2 * n - 2:
        if amida[i][pos + 1] == '-':
            i -= 1
            pos += 2
            continue
    i -= 1
print(pos//2+1)
