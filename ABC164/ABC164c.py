# ABC164c


def main():
    import sys
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))


if __name__ == '__main__':
    main()
