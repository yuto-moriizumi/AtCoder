n = (int)(input())
a = (int)(input())
b = (int)(input())
c = (int)(input())
d = (int)(input())
e = (int)(input())

toshi1 = n
toshi2 = 0
toshi3 = 0
toshi4 = 0
toshi5 = 0
toshi6 = 0
time = 0

while (toshi6 < n):
    i = 0
    while(i < e and toshi5 > 0):
        toshi5 = toshi5 - 1
        toshi6 = toshi6 + 1
        i = i + 1
    i = 0
    while(i < d and toshi4 > 0):
        toshi4 = toshi4 - 1
        toshi5 = toshi5 + 1
        i = i + 1
    i = 0
    while(i < c and toshi3 > 0):
        toshi3 = toshi3 - 1
        toshi4 = toshi4 + 1
        i = i + 1
    i = 0
    while(i < b and toshi2 > 0):
        toshi2 = toshi2 - 1
        toshi3 = toshi3 + 1
        i = i + 1
    i = 0
    while(i < a and toshi1 > 0):
        toshi1 = toshi1 - 1
        toshi2 = toshi2 + 1
        i = i + 1
    time = time + 1
    print(time, toshi1, toshi2, toshi3, toshi4, toshi5, toshi6)
print(time)
