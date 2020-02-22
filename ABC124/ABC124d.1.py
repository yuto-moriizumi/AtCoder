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
    sll = len(sl)
    cl = []
    c = 0
    for i in range(n):
        st = i-k
        ed = i + k+1
        if (st < 0):
            st = 0
        if (k % 2 == 1 and i % 2 == 0 or k % 2 == 0 and i % 2 == 1):  # kが奇数の時、0の箇所（すなわちiが偶数の箇所）を中心に反転
            if (c == 0):
                cl.append(sum(sl[st: ed]))
            else:
                t = cl[c - 1]
                if(ed <= sll):
                    t += sum(sl[ed - 2: ed])
                if (st > 0):
                    cst = st-2
                    if (cst < 0):
                        cst = 0
                    t -= sum(sl[cst: st])
                cl.append(t)
                c += 1

    print(max(cl))
else:
    print(1)
