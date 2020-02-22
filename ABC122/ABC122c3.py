import sys
input = sys.stdin.readline
n, q = map(int, input().split())
s = input()

count = [0]
for i in range(1, n):
    count.append(count[i-1])
    if(s[i-1:i+1] == "AC"):
        count[i] += 1

# print(count)

for _ in range(q):
    l, r = map(int, input().split())
    print(count[r-1]-count[l-1])
