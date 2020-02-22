# ABC145b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    n = int(input())
    s = input()[:-1]
    print('Yes' if s[:n//2] == s[n//2:] else 'No')


if __name__ == '__main__':
    main()
