# ABC168b


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    k = int(input())
    s = input()
    if (len(s) <= k):
        print(s)
    else:
        print(s[:k]+'...')


if __name__ == '__main__':
    main()
