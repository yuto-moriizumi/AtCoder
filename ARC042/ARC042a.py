# ARC042a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    from operator import itemgetter
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    kl = [[i, 0] for i in range(n)]

    for i in range(m):
        kl[a[i] - 1][1] = i+1
    kl.sort(key=itemgetter(1), reverse=True)
    print(*[i[0]+1 for i in kl], sep='\n')


if __name__ == '__main__':
    main()
