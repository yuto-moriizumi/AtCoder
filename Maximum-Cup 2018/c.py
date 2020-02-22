def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # map(int, input().split())
    n = int(input())
    edge = [0]*n
    color = [-1]*n
    flag = False

    for i in range(n):
        edge[i] = int(input())-1

    def dfs(i, pre, c):
        if color[i] == c:
            return False
        elif color[i] == 1-c:
            return True
        color[i] = c
        return dfs(edge[i], i, 1-c)

    for i in range(n):
        if color[i] == -1:
            flag = flag or dfs(i, -1, 0)
    if not flag:
        print(max(color.count(0), color.count(1)))
    else:
        print(-1)
    #print(color)


if __name__ == '__main__':
    main()
