n, k = map(int, input().split())
s = input()

if(n != 1):
    sl = []
    c = 1
    if (s[0] == "1"):
        sl.append(0)
    for i in range(n):
        if (i != 0):
            if (s[i] == s[i-1]):
                c += 1
            else:
                sl.append(c)
                c = 1
    sl.append(c)

    cl = []
    for i in range(n):
        st = i - k
        ed = i + k+1
        if (st < 0):
            st = 0
        if (ed > len(sl)):
            ed = len(sl)
        if (k % 2 == 1):  # kが奇数の時、0の箇所（すなわちiが偶数の箇所）を中心に反転
            if (i % 2 == 0):
                cl.append(sum(sl[st:ed]))
        else:  # kが偶数の時、1の箇所（すなわちiが奇数の箇所）を中心に反転
            if (i % 2 == 1):
                cl.append(sum(sl[st:ed]))

    print(max(cl))
else:
    print(1)
