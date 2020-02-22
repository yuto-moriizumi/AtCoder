n = int(input())
xCount = 0
oCount = 0
indexes = set()
for i in range(n):
    fumen = list(input())
    xCount += fumen.count('x')
    li = 0
    lindexes = indexes
    indexes = set()
    while True:
        try:
            ind = fumen.index('o', li)
        except:
            break
        if ind != -1:
            li = ind+1
            indexes.add(ind)
            continue
        break
    oCount += len(indexes)-len(lindexes.intersection(indexes))
print(xCount+oCount)
