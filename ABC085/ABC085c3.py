n, y = map(int, input().split())

for a in range(n + 1):
    for b in range(n - a + 1):
        if (y - a * 10000 - b * 5000 == (n - a - b)*1000):
            print(a, b, n - a - b)
            exit()
print(-1, -1, -1)
