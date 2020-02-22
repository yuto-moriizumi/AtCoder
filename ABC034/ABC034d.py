# ABC034d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
yoki = [tuple(map(int, input().split())) for _ in range(n)]


def evaluate(number):
    siomizu = []
    for w, p in yoki:
        salt = w * p / 100
        siomizu.append(salt - number * w)
    siomizu.sort(reverse=True)
    wa = sum(siomizu[:k])
    if wa > 0:  # もっと高い値を探せ
        return 1
    if wa == 0:  # まさにこの値
        return 0
    if wa < 0:  # もっと低い値を探せ
        return - 1


def binary_search(low, high):
    lowest = low
    highest = high
    while high-low >= 10**-12:  # high-low >= 10**-12 ←これ以下の誤差を許容
        mid = (low + high) / 2
        guess = evaluate(mid)
        if guess == 0:
            return [mid, mid]
        if guess < 0:
            high = mid  # 連続値の場合mid
            highest = mid
        else:
            low = mid  # 連続値の場合mid
            lowest = mid

    return [lowest, highest]


print(binary_search(0, 100)[1]*100)
