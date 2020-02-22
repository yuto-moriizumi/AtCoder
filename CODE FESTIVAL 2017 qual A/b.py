def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, m, k = map(int, input().split())

    for i in range(n + 1):
        for j in range(m + 1):
            if j*n+i*m-i*j-j*i == k:
                #print(i, j)
                print('Yes')
                exit(0)
    print('No')


if __name__ == '__main__':
    main()
