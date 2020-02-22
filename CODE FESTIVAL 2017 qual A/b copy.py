def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n, m, k = map(int, input().split())

    for i in range(n + 1):
        if ((k-i*m)/(n-2*i))*n+i*m-i*((k-i*m)/(n-2*i))-((k-i*m)/(n-2*i))*i == k:
            #print(i, j)
            print('Yes')
            exit(0)
    print('No')


if __name__ == '__main__':
    main()
