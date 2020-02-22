# ABC156a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, r = map(int, input().split())
    if n >= 10:
        print(r)
    else:
        print(100*(10-n)+r)


if __name__ == '__main__':
    main()
