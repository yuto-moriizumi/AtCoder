# ABC155a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    import collections

    if len(collections.Counter(list(map(int, input().split()))).most_common()) == 2:
        print('Yes')
        exit(0)
    print('No')


if __name__ == '__main__':
    main()
