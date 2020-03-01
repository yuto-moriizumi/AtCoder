# ABC157c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, m = map(int, input().split())
    con = [list(map(int, input().split())) for _ in range(m)]
    num = ['a'] * n
    for s, c in con:
        if num[s - 1] == 'a' or num[s - 1] == c:
            num[s - 1] = str(c)
            continue
        print(-1)
        exit(0)
    for i in range(n):
        if num[i] == 'a':
            if i == 0:
                num[i] = '1'
            else:
                num[i] = '0'
    if num[0] == '0':
        print(-1)
        exit(0)
    print(*num, sep='')


if __name__ == '__main__':
    main()
