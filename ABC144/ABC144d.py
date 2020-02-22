# ABC144d


def main():
    import sys
    import math
    #import numpy as np
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    a, b, x = map(int, input().split())
    if x > a*a*b/2:
        # print(np.rad2deg(np.arctan(2*(a*a*b-x)/(a*a*a))))
        print(math.degrees(math.atan(2*(a*a*b-x)/(a*a*a))))
        exit(0)
    print(math.degrees(math.atan(a*b*b/2/x)))
    # print(np.rad2deg(np.arctan(a*b*b/2/x)))


if __name__ == '__main__':
    main()
