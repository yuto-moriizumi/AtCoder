n = int(input())
w = list(input().split())

s1 = 'takahashikun'
s2 = s1.capitalize()
s3 = s1.upper()
ans = 0
for word in w:
    if word[-1] == '.':
        word = word[:-1]
    if word in (s1, s2, s3):
        ans += 1
print(ans)
