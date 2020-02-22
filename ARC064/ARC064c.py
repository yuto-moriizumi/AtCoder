# ARC064c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ooi = a[i] + a[i + 1] - x
        #print(i, ooi)
        if ooi > 0:
            before = a[i + 1]
            #print(i, 'before', a[i + 1])
            a[i + 1] = max(0, a[i + 1] - ooi)
            #print(i, 'after', a[i + 1])
            ans += before - a[i + 1]
            #print(i, 'ans', ans)

            ooi = a[i] + a[i + 1] - x
            if ooi > 0:
                before = a[i]
                a[i] = max(0, a[i] - ooi)
                ans += before - a[i]
    print(ans)


if __name__ == '__main__':
    main()
