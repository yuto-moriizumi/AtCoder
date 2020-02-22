# ABC144c


def main():
    import sys
    import math
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    n = int(input())
    ans = 10**12
    for i in range(math.ceil(math.sqrt(n))+1, 0, -1):
        if n % i == 0:
            ans = min(ans, i+n//i)
    print(ans-2)


if __name__ == '__main__':
    main()
