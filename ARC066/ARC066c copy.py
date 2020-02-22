def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # print(a)
    if(n % 2 == 0):
        for i in range(n-1):
            if i % 2 == 0 and a[i] != a[i+1] or i % 2 == 1 and a[i]+2 != a[i+1]:
                print(0)
                exit(0)
        print(2**(n//2) % (10**9+7))
        exit(0)
    if a[0] != 0:
        print(0)
        exit(0)
    for i in range(1, n-1):
        if i % 2 == 0 and a[i]+2 != a[i+1] or i % 2 == 1 and a[i] != a[i+1]:
            print(0)
            exit(0)
    print(2**((n-1)//2) % (10**9+7))
    exit(0)


if __name__ == '__main__':
    main()
