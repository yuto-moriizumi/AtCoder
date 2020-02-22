# ABC147c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n = int(input())
    x = []
    aa = []
    for _ in range(n):
        a = int(input())
        aa.append(a)
        x.append([list(map(int, input().split())) for _ in range(a)])

    # map(int,input().split())

    tadasii = [-1] * n
    tadasii[0] = True
    flag = False
    setu = 0
    for i in range(n):
        for p, y in x[i]:
            target = None
            if tadasii[i]:
                target = True if y == 1 else False
            if not tadasii[i]:
                target = False if y == 1 else True
            if tadasii[p - 1] == -1 or tadasii[p - 1] == target:
                tadasii[p - 1] = target
            else:
                flag = True
                break
    if not flag:
        setu = tadasii.count(True)
    else:
        setu = 0

    tadasii = [-1] * n
    tadasii[0] = False
    flag = False
    setu2 = 0
    for i in range(n):
        for p, y in x[i]:
            target = None
            if tadasii[i]:
                target = True if y == 1 else False
            if not tadasii[i]:
                target = False if y == 1 else True
            if tadasii[p - 1] == -1 or tadasii[p - 1] == target:
                tadasii[p - 1] = target
            else:
                flag = True
                break
    if not flag:
        setu2 = tadasii.count(True)
    else:
        setu2 = 0

    print(max(setu, setu2))


if __name__ == '__main__':
    main()
