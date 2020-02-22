# ABC141e
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
kagi = []
for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    kagi.append([a, b, c, i])

takara = [[-1, -1] for _ in range(n + 1)]


for i in kagi:
    for j in i[2]:
        if (takara[j][0] == -1 or i[0]/i[1] < takara[j][0]):
            takara[j][0] = i[0]/i[1]
            takara[j][1] = i[3]
# print(takara)
used = set()
ans = 0
for i in range(1, len(takara)):
    if takara[i][1] == -1:
        print(-1)
        exit()
    if not takara[i][1] in used:
        ans += kagi[takara[i][1]][0]
        used.add(takara[i][1])
print(ans)
