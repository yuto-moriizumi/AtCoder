# AGC007a
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    h, w = map(int, input().split())

    grid = [input()[:-1] for _ in range(h)]

    def dfs(i, j):
        cou = 0
        if i == h-1 and j == w-1 or i == h-2 and j == w-1 or i == h-1 and j == w-2:
            print('Possible')
            exit(0)
        if i < h-1 and grid[i+1][j] == '#':
            cou += 1
        if j < w-1 and grid[i][j+1] == '#':
            cou += 1
        if cou != 1:
            print('Impossible')
            exit(0)
        if i < h-1 and grid[i+1][j] == '#':
            dfs(i+1, j)
        if j < w-1 and grid[i][j+1] == '#':
            dfs(i, j+1)

    dfs(0, 0)
    print('Impossible')


if __name__ == '__main__':
    main()
