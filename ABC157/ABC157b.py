# ABC157b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと
    bing = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    b = [int(input()) for _ in range(n)]
    for num in b:
        for i in bing:
            try:
                while True:
                    t = i.index(num)
                    i[t] = -1
            except:
                continue
    # print(bing)

    naname = [((0, 0), (1, 1), (2, 2)), (2, 0), (1, 1), (0, 2)]
    if sum(bing[0]) == -3 or sum(bing[1]) == -3 or sum(bing[2]) == -3 or bing[0][0]+bing[1][0]+bing[2][0] == -3 or bing[0][1]+bing[1][1]+bing[2][1] == -3 or bing[0][2]+bing[1][2]+bing[2][2] == -3 or bing[0][0]+bing[1][1]+bing[2][2] == -3 or bing[0][2]+bing[1][1]+bing[2][0] == -3:
        print('Yes')
        exit(0)

    print('No')


if __name__ == '__main__':
    main()
