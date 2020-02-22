import sys
input = sys.stdin.readline

p = list(map(int, input().split()))

result = []
for i in range(len(p)):
    for j in range(i+1, len(p)):
        result.append(p[i] + p[j])

print(min(result))
