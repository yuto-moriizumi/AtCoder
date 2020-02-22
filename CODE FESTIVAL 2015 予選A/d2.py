N, m = map(int, input().split())
x = [int(input()) for _ in range(m)]
x.sort()
d = [0]*(m+1)  # i番目（1-indexed）の人が何両目まで点検できるか


def evaluate(n):
    for i in range(m):
        l = x[i] - d[i] - 1
        R = 0
        for r in range(n+1):
            if min(l * 2 + r, l + r * 2) <= n:
                if i + 1 < m:
                    if x[i] + r < x[i + 1]:
                        R = r
                    else:
                        break
                else:
                    R = r
            else:
                break
        if R < 0:
            return 1
        d[i+1] = x[i]+R
    if d[m] < N:  # もっと高い値を探せ
        return 1
    # if d[m] == N:  # まさにこの値
    #    return 0
    if d[m] >= N:  # もっと低い値を探せ
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


print(binary_search(0, N*2))
