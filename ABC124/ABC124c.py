s = list(input())
c = 0
for i in range(len(s)):
    if (i != 0):
        if (s[i] == s[i - 1]):
            c += 1
            if (s[i] == "0"):
                s[i] = "1"
            else:
                s[i] = "0"
print(c)
