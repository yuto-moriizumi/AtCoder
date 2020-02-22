n = int(input())
a = list(map(int, input().split()))


def calc(l, to):
    cost = 0
    for i in l:
        cost += (i-to)**2
    return cost


ans = 10**9
for i in range(-100, 101):
    ans = min(ans, calc(a, i))
print(ans)
