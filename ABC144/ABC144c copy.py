# ABC144c
import math


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # map(int,input().split())
    n = int(input())
    ans = 10**12
    for i in range(n//2+1):
        for j in range(n//2+1):
            if(i*j == n):
                ans = min(ans, i+j)
    print(ans-2)


if __name__ == '__main__':
    main()
