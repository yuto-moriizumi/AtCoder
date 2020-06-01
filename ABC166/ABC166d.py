# ABC166d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    x = int(input())
    for i in range(-200, 200):
        for j in range(-200, 200):
            if (i ** 5 - j ** 5 == x):
                print(i, j)
                exit(0)


if __name__ == '__main__':
    main()
