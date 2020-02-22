# ABC135b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p = list(map(int, input().split()))
# print(p)
# print(p2)
#print(p == p2)

for i in range(len(p)):
    for j in range(i, len(p)):
        p2 = sorted(p)
        tmp = p2[i]
        p2[i] = p2[j]
        p2[j] = tmp
        if (p == p2):
            print("YES")
            exit()
print("NO")
