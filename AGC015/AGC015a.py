# AGC015a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, a, b = map(int, input().split())
    if b-a < 0:
        print(0)
        exit(0)
    if n == 1:
        if b != a:
            print(0)
        else:
            print(1)
        exit(0)
    print((n-2)*(b-a)+1)


if __name__ == '__main__':
    main()
