# ABC018d
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, p, q, r = map(int, input().split())
choco = [list(map(int, input().split())) for _ in range(r)]
group = set()


def calc():
    # print(group)
    score = [[0, i] for i in range(m)]
    for x, y, z in choco:
        if x-1 in group:
            score[y - 1][0] += z
    score.sort(reverse=True)
    ans = 0
    for i in score[:q]:
        ans += i[0]
    return ans


def select(i, ninzu):
    if i > n:
        return 0
    if ninzu == p:
        return calc()
    group.add((i))
    ans = select(i + 1, ninzu + 1)
    group.remove((i))
    return max(ans, select(i+1, ninzu))


print(select(0, 0))
