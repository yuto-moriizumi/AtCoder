n = (int)(input())
a = (int)(input())
b = (int)(input())
c = (int)(input())
d = (int)(input())
e = (int)(input())

time = 0
array = a, b, c, d, e
ind = array.index(min(array))
time = - (-n // array[ind])
time = ind+time+(4-ind)
print(time)
