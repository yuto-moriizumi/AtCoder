# ABC006d
import sys
import bisect
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    n = int(input())
    c = [int(input()) for _ in range(n)]

    # dp[i]=長さがiであるような増加部分列のうち、最も小さい最後の数字
    dp = [10 ** 10] * (n + 1)
    dp[0] = 0
    for j in range(n):
        #print(c[j], bisect.bisect(dp, c[j]))
        dp[bisect.bisect(dp, c[j])] = c[j]
    # print(dp)
    print(dp.count(10 ** 10))
    # print(dp)


if __name__ == '__main__':
    main()
