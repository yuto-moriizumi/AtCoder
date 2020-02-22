# AGC004a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    a, b, c = map(int, input().split())

    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print(0)
        exit(0)
    print(min(a*b, b*c, c*a))


if __name__ == '__main__':
    main()
