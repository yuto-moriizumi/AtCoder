
def prime_numbers(right):
    if right <= 2:
        return []
    pn = [2]
    for L in range(3, right):
        chk = True
        for L2 in pn:
            if L % L2 == 0:
                chk = False
        if chk == True:
            pn.append(L)
    return pn


print(len(prime_numbers(int(input()))))
