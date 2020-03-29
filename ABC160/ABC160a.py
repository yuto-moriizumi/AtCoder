# ABC160a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    s = input()
    if s[2] == s[3] and s[4] == s[5]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
