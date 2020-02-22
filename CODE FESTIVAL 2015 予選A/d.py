from math import floor
N, m = map(int, input().split())
x = [int(input()) for _ in range(m)]
x.sort()
d = [0]*(m+1)  # i番目（1-indexed）の人が何両目まで点検できるか


def evaluate(n):
    for i in range(m):
        l = x[i] - d[i] - 1
        r = max(n - 2 * l, (n - l) // 2)
        if r < 0:
            return 1
        if i+1 < m:
            r = min(r, x[i + 1] - x[i] - 1)
        d[i + 1] = x[i] + r
        #print(n, x[i], l, r, d[i + 1])
    if d[m] < N:  # もっと高い値を探せ
        return 1
    # if d[m] == N:  # まさにこの値
    #    return 0
    if d[m] >= N:  # もっと低い値を探せ
        #print(n, d)
        return - 1


def binary_search(low, high):
    lowest = low
    highest = high
    while low <= high:  # high-low >= 10**-12 ←これ以下の誤差を許容
        mid = (low + high) // 2
        guess = evaluate(mid)
        if guess == 0:
            return [mid, mid]
        if guess < 0:
            high = mid - 1  # 連続値の場合mid
            highest = mid
        else:
            low = mid + 1  # 連続値の場合mid
            lowest = mid

    return [lowest, highest]


print(binary_search(0, N*2)[1])
