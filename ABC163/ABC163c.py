# ABC163c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    from collections import Counter

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    a = list(map(int, input().split()))
    a = Counter(a)
    for i in range(n):
        print(a[i+1])


if __name__ == '__main__':
    main()
