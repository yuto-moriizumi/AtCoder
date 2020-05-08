# ABC165a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    k = int(input())
    a, b = map(int, input().split())
    if k == 1:
        print('OK')
        exit(0)
    for i in range(b // k + 2):
        if a <= i * k <= b:
            print('OK')
            exit(0)
    print('NG')


if __name__ == '__main__':
    main()
