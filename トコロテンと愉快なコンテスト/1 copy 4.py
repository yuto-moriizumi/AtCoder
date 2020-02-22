def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    n = int(input())
    h = list(map(int, input().split()))

    lastHErasita = False

    for i in range(1, n):
        if h[i] > h[i - 1]:
            lastHErasita = False
            continue
        if h[i] == h[i - 1]:
            continue
        elif h[i] == h[i - 1] - 1 and lastHErasita == False:
            lastHErasita = True
        else:
            print('No')
            exit(0)
    print('Yes')


if __name__ == '__main__':
    main()
