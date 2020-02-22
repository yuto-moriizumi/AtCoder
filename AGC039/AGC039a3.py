# AGC039a
def main():
    import distutils.sysconfig
    # map(int, input().split())

    s = input()
    k = int(input())
    s2 = s
    s = list(s)
    s2 = list(s2)

    if (len(set(s)) == 1):
        print(len(s) * k // 2)
        exit(0)

    ans = 0
    targ = ''
    cou = 1
    flag = True
    for i in range(len(s)):
        if s[i] == targ:
            cou += 1
            if i == len(s) - 1 and cou % 2 == 0:
                flag = False
            continue
        ans += cou // 2
        cou = 1
        targ = s[i]
    ans += cou // 2
    cou = 1

    ans *= k

    if s2[0] == s2[-1]:
        f = s2[0]
        a = -1
        for i in s2:
            if i != f:
                break
            a += 1
        f = s2[-1]
        b = -1
        for i in s2[::-1]:
            if i != f:
                break
            b += 1
        ans -= (a//2 + b//2)*(k-1)
        ans += (a+b)//2*(k - 1)
    print(ans)


if __name__ == '__main__':
    main()
