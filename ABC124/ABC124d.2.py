n, k = map(int, input().split())
s = str(input())

sl = []
c = 1
if (s[0] == "1"):
    sl.append(0)
for i in range(n):
    if (i != 0):
        if (s[i] == s[i-1]):
            c += 1
        else:
            sl.append(c)
            c = 1
sl.append(c)

ruisekiwa = [0]
sums = []
ans = 0
w = 2*k+1

if (w > len(sl)):
    print(n)
    exit()
for i in range(len(sl)):
    ruisekiwa.append(ruisekiwa[i] + sl[i])
# print(sl)
# print(ruisekiwa)
for i in range(len(sl)):
    if(k % 2 == 1 and i % 2 == 0 or k % 2 == 0 and i % 2 == 1):
        left = i-k
        if (left < 0):
            left = 0
        right = i + k+1
        if (right >= len(ruisekiwa)):
            right = len(ruisekiwa)-1
        # print(ruisekiwa[right], "-", ruisekiwa[left],
        #      "=", ruisekiwa[right]-ruisekiwa[left])
        ans = max(ans, ruisekiwa[right]-ruisekiwa[left])
print(ans)
