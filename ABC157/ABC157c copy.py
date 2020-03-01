# ABC157c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, m = map(int, input().split())
    con = [list(map(int, input().split())) for _ in range(m)]
    s = 10 ** (n - 1)
    if s == 1:
        s -= 1

    for i in range(s, 10 ** (n + 1)):
        falg = False
        num = list(str(i))
        for s, c in con:
            if num[s - 1] != str(c):
                falg = True
                break
        if falg:
            continue
        print(*num, sep='')
        exit(0)
    print(-1)


if __name__ == '__main__':
    main()
