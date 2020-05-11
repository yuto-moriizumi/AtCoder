# ABC167a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    s = input()
    t = input()
    if len(s) + 1 != len(t):
        print('No')
        exit(0)
    if s != t[:-1]:
        print('No')
        exit(0)
    print('Yes')


if __name__ == '__main__':
    main()
