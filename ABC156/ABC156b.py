# ABC156b


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, k = map(int, input().split())
    ans = []
    for i in range(30, -1, -1):
        t = n//k**i
        if len(ans) == 0 and t == 0:
            continue
        ans.append(t)
        n = n-k**i*t
    print(len(ans))


if __name__ == '__main__':
    main()
