n = (int)(input())
a = (int)(input())
b = (int)(input())
c = (int)(input())
d = (int)(input())
e = (int)(input())

time = 0
array = a, b, c, d, e
while(len(array) != 0):
    ind = array.index(min(array))
    if(- (-n // array[ind]) < time):
        time = time + 1
    else:
        time = time - (-n // array[ind])
    array = array[ind + 1:]
    print(array, time)
print(time)
