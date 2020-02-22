s = input()
k = int(input())

ans = set()
for i in range(len(s)):
    for j in range(1, k+1):
        ans.add(s[i:i+j])

# print(ans)
print(sorted(list(ans))[k-1])
