def main():
    # 最初に入れておくとinputが早くなる
    import sys
    input = sys.stdin.readline

    # スタック最大数をセット
    sys.setrecursionlimit(10 ** 6)

    d = int(input())
    n = int(input())
    Ns = list(map(int, list(str(n))))
    MOD = 10**9+7

    # i番目を見て今のところ和の剰余がmodでi番目を自由に決めていいか→その場合の数

    dp = [[[-1]*2 for i in range(d)] for j in range(len(Ns)+1)]
    # print(dp)

    def calc(i, mod, isFree):
        # print(i, mod, isFree)
        if (i == len(Ns)):
            return 1 if mod == 0 else 0
        if (dp[i][mod][isFree] != -1):
            return dp[i][mod][isFree]
        ans = 0
        for j in range(10):
            if (isFree == 0 and Ns[i] < j):
                break
            ans = (calc(i + 1, (mod + j) %
                        d, 1 if isFree == 1 or Ns[i] != j else 0) + ans) % MOD
        dp[i][mod][isFree] = ans
        return ans

    print((calc(0, 0, 0) - 1) % MOD)
    print(dp)

    # ここに書く
if __name__ == '__main__':
    main()
