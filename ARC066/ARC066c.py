def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if(n % 2 == 0):
        for i in range(1, n, 2):
            if(a[i-1:i+1].count(i) != 2):
                print(0)
                exit(0)
        print(2**(n//2))
        exit(0)
    for i in range(0, n, 2):
        if(i == 0 and a[0:2].count(i) != 1):
            print(0)
            exit(0)
        elif(i != 0 and a[i-1:i+1].count(i) != 2):
            print(0)
            exit(0)
    print(2**(n//2))


if __name__ == '__main__':
    main()
