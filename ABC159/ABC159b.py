# ABC159b


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    s = input()
    n = len(s)
    if s != s[::-1]:
        print('No')
        exit(0)
    if s[: (n - 1) // 2] != s[: (n - 1) // 2:-1]:
        print('No')
        exit(0)
    if s[(n+3)//2-1:n] != s[(n+3)//2-1:n][::-1]:
        print('No')
        exit(0)
    print('Yes')


if __name__ == '__main__':
    main()
