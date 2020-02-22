# ARC069c
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m = map(int, input().split())
    if m > n*2:
        print(n+(m-n*2)//4)
    else:
        print(m//2)


if __name__ == '__main__':
    main()
