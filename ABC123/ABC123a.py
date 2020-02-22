a = [0, 0, 0, 0, 0]
for i in range(5):
    a[i] = (int)(input())
k = (int)(input())
isExist = "Yay!"

for d in [d+1 for d in range(4)]:
    for i in range(4):
        if i + d < 5 and (a[i+d] - a[i] > k):
            isExist = ":("

print(isExist)
