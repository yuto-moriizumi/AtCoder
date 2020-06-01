# ABC168a


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = input()
    if n[-1] in '24579':
        print('hon')
    elif n[-1] in '0168':
        print('pon')
    else:
        print('bon')


if __name__ == '__main__':
    main()
