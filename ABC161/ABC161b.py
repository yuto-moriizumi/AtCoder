# ABC161b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    s = sum(a)
    for i in a:
        if i >= s / 4 / m:
            ans += 1
    if ans >= m:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
