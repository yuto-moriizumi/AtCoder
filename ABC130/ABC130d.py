#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

ruisekiwa = [0]

for i in range(1,n+1):
    ruisekiwa.append(ruisekiwa[i - 1] + a[i-1])

count = 0
i = 0
j = 0

#print(ruisekiwa)
while(i<n+1):
    if (ruisekiwa[i] - ruisekiwa[j] >= k):
        count += n-i+1
        j += 1
    else:
        i += 1
print(count)