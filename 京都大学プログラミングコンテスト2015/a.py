t = int(input())
s = [input() for _ in range(t)]
last = 0
ans = [0]*t
i = 0
while(i < t):
    idx = s[i].find('tokyo', last)
    idx2 = s[i].find('kyoto', last)
    if (idx == -1):
        if (idx2 == -1):
            i += 1
            last = 0
        else:
            last = idx2 + 5
            ans[i] += 1
    else:
        if (idx2 == -1):
            last = idx + 5
            ans[i] += 1
        else:
            last = min(idx, idx2) + 5
            ans[i] += 1
    # print(idx)
for i in ans:
    print(i)
