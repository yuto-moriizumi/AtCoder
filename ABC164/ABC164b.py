# ABC164b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    a, b, c, d = map(int, input().split())

    turn = 0
    while a > 0 and c > 0:
        if turn == 0:
            c -= b
        else:
            a -= d
        #print(a, c)
        turn = 1 - turn
    if a > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
