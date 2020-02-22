n = int(input())
s = input()
t = input()

for zurasu in range(0, n+1):
    if s[zurasu:] == t[:n-zurasu]:
        print(n+zurasu)
        exit(0)
