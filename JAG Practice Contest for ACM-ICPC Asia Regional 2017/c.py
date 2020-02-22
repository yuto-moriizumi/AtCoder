l, r = map(int, input().split())
isPrime = [0]*(r+1)


def prime_numbers(right):
    pn = [2]
    for L in range(3, right):
        chk = True
        for L2 in pn:
            if L % L2 == 0:
                chk = False
        if chk == True:
            pn.append(L)
            isPrime[L] = 1


prime_numbers(r+1)
isPrime[2] = 1


def cum(array):
    result = [0]
    for i in range(len(array)):
        result.append(array[i]+result[i])
    return result


result = cum(isPrime)

print(result[r+1]-result[l])
print(isPrime)
print(result)
