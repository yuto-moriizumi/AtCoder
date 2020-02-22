n = int(input())
s = input()
t = input()

pos = 0
ans = n*2
for pos in range(n):
    if s[pos:] == t[:n-pos]:
        ans = n+pos
        break
print(ans)
n