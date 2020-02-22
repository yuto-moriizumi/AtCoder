def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    h, w = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    dx = [1, -1]
    mode = 0
    ans = [[0]*w for _ in range(h)]
    x = 0
    y = 0
    i = 0
    while(0 <= y < h):
        while(0 <= x < w):
            if(a[i] > 0):
                ans[y][x] = i+1
                x += dx[mode]
                a[i] -= 1
            else:
                i += 1
        y += 1
        mode = 1-mode
        x += dx[mode]
    for i in ans:
        print(*i)


if __name__ == '__main__':
    main()
