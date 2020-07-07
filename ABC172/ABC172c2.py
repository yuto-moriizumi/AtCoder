# ABC172c


def main():
    import sys
    import bisect
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    def cum(array):  # result[i]=i番目まで（1-indexed）の累積和
        result = [0]
        for i in range(len(array)):
            result.append(array[i]+result[i])
        return result

    bc = cum(b)
    ac = cum(a)
    ans = 0
    for i in range(n + 1):
        if ac[i] <= k:
            #print(i, bisect.bisect_left(bc, k - ac[i])-1)
            ans = max(ans, i + bisect.bisect_right(bc, k - ac[i])-1)
    print(ans)


if __name__ == '__main__':
    main()
