s = input().split()
n = int(input())
t = [input() for _ in range(n)]


def match(s1, reg):
    if len(s1) != len(reg):
        return False
    for i in range(len(s1)):
        if reg[i] != '*' and reg[i] != s1[i]:
            return False
    return True


for i in range(len(s)):
    for reg in t:
        if match(s[i], reg):
            s[i] = '*' * len(s[i])
            break

print(*s)
