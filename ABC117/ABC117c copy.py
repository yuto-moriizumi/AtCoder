def main():
    # ABC117c
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    if(m == 1):
        print(0)
        exit(0)
    if(n >= m):
        print(0)
        exit(0)
    x.sort()
    sa = [0]
    for i in range(1, m):
        sa.append(x[i]-x[i-1])
    # print(x)
    # print(sa)
    # print('aa')
    sa.sort()
    # or _ in range(min(n-1, len(sa)-1)):
    #    sa = sa[:-1]
    # print(sa)
    print(sum(sa[:len(sa)-min(n-1, len(sa)-1)]))


if __name__ == '__main__':
    main()
