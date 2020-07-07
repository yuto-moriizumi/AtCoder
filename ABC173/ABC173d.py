# ABC173d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    ans = a[0]
    last1 = a[1]
    last2 = a[1]
    for i in range(2, n):
        if last1 < last2:
            ans += last2
            last2 = a[i]
        else:
            ans += last1
            last1 = a[i]
    print(ans)


if __name__ == '__main__':
    main()
