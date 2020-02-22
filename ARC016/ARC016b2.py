n = int(input())
grid = [list(input()) for _ in range(n)]
ans = 0
for j in range(n):
    for i in range(len(grid[j])):
        if grid[j][i] == 'x':
            ans += 1
        elif grid[j][i] == 'o':
            if 0 < j:
                if grid[j-1][i] != 'o':
                    ans += 1
            else:
                ans += 1
print(ans)
