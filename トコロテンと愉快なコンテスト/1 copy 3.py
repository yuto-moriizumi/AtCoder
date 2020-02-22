def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    k, x = map(int, input().split())
    for i in range(x - k+1, x + k):
        print(i, end=' ')


if __name__ == '__main__':
    main()
