# ABC155b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n = int(input())
    a = list(map(int, input().split()))

    for i in a:
        if i % 2 == 0:
            if i % 3 == 0 or i % 5 == 0:
                continue
            else:
                print('DENIED')
                exit(0)
    print('APPROVED')


if __name__ == '__main__':
    main()
