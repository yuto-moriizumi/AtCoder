# ABC162a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = input()
    if n.find('7') != -1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
