import sys
input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
ruiseki = [0]
for i in range(len(w)):
    ruiseki.append(ruiseki[i] + w[i])
result = []
for i in range(1, len(w)):
    result.append(abs(ruiseki[i]-(ruiseki[-1]-ruiseki[i])))
# print(ruiseki)
print(min(result))
