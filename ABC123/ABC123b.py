a = (int)(input())
b = (int)(input())
c = (int)(input())
d = (int)(input())
e = (int)(input())

at = -(-a//10)*10
bt = -(-b//10)*10
ct = -(-c//10)*10
dt = -(-d//10)*10
et = -(-e//10)*10

aa = a % 10
ba = b % 10
ca = c % 10
da = d % 10
ea = e % 10

array = (aa, ba, ca, da, ea)
minn = aa
for i in array:
    if (i != 0 and minn > i):
        minn = i
test = array.index(minn)

if (test == 0):
    time = a + bt + ct + dt + et
elif (test == 1):
    time = at + b + ct + dt + et
elif (test == 2):
    time = at + bt + c + dt + et
elif (test == 3):
    time = at + bt + ct + d + et
elif (test == 4):
    time = at + bt + ct + dt + e

print(time)
