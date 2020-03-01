# ABC157a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    n = int(input())
    from math import ceil
    print(ceil(n/2))


if __name__ == '__main__':
    main()
