# ABC154d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    pos = 0

    def cum(array):
        result = [0]
        for i in range(len(array)):
            result.append(array[i]+result[i])
        return result

    def calc(N):
        t = 0
        for i in range(1, N+1):
            t += i / N
        return t

    p2 = cum(p)

    for i in range(n - k+1):
        if ans < p2[i+k]-p2[i]:
            ans = p2[i+k]-p2[i]
            pos = i

    ans = 0
    for i in range(pos, pos + k):
        ans += calc(p[i])
    print(ans)


if __name__ == '__main__':
    main()
