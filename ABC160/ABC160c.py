# ABC160c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in a:
        b.append(i - k)
    b.extend(a)
    ans = 10 ** 12
    # print(b)
    for i in range(n):
        #print(i, b[i+n-1], b[i])
        ans = min(ans, b[i+n-1]-b[i])
    print(ans)


if __name__ == '__main__':
    main()
