import itertools

n = int(input())
p = list(map(int, input().split()))

ans = set()

for i in range(n+1):
    for j in itertools.combinations(p, i):
        ans.add(sum(j))

print(len(ans))
