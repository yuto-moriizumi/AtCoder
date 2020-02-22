import sys
input = sys.stdin.readline

r, d, x = map(int, input().split())
ans = [r*x-d]

print(ans[0])
for i in range(0, 9):
    ans.append(ans[i]*r-d)
    print(ans[i+1])
