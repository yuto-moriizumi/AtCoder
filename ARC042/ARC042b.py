# ARC042b
def main():
    import sys
    import numpy as np
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    X, Y = map(int, input().split())
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]

    ans = 10**12

    for i in range(1, n+1):
        p1 = p[i - 1]
        p2 = p[i % n]
        #print('p', p1, p2)
        v1 = np.array([X - p1[0], Y - p1[1]])
        v2 = np.array([p2[0] - p1[0], p2[1] - p1[1]])
        #print('v', v1, v2)
        ans = min(ans, abs(np.cross(v1, v2)/np.linalg.norm(v2)))
    print(ans)


if __name__ == '__main__':
    main()
