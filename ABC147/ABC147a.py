# ABC147a


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    a = list(map(int, input().split()))
    print('bust' if sum(a) > 21 else 'win')


if __name__ == '__main__':
    main()
