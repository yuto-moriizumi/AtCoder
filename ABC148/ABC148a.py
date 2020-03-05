# ABC148a

import logging


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    def dump(*args):
        sys.stderr.write(str(args))
    # 再帰関数を使わない限りPypyで出すこと

    print('a' & 1)


    a = int(input())
    b = int(input())
    print(*set([1, 2, 3]).difference(set([a]), set([b])))


if __name__ == '__main__':
    main()
