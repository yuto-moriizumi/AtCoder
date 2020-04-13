# ABC162b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if not (i % 3 == 0 or i % 5 == 0):
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
