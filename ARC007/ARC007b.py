n, m = map(int, input().split())
disk = [int(input()) for _ in range(m)]
case = [i for i in range(n+1)]

for i in range(m):
    tmp = case[0]
    place = case.index(disk[i])
    case[0] = disk[i]
    case[place] = tmp

for i in case[1:]:
    print(i)
