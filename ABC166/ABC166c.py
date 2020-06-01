# ABC166c


from operator import itemgetter


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, t = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in a:
        i.append(i[0]-i[1])
    a.sort(key=itemgetter(2), reverse=True)

    now = sum([i[0] for i in a])
    i = 0
    while now > t and i < n:
        now -= a[i][2]
        i += 1
    #print(a)
    if now > t:
        print(-1)
    else:
        print(i)


if __name__ == '__main__':
    main()
