import sys
input = sys.stdin.readline

memoCou = {}

n = int(input())


def cou(n, s):
    if(memoCou.get((n, s)) != None):
        return memoCou.get((n, s))
    if(not ok(s)):
        return 0
    #print(n, s)
    if(n == 0):
        return 1
    memoCou.update({(n, s): cou(
        n-1, s[1:]+"A")+cou(n-1, s[1:]+"C")+cou(n-1, s[1:]+"G")+cou(n-1, s[1:]+"T")})
    return memoCou.get((n, s))


def ok(s):
    for i in range(4):
        t = list(s)
        if(i < 3):
            t[i], t[i+1] = t[i+1], t[i]
        if("".join(t).count("AGC") >= 1):
            return False
    return True


print(cou(n, "TTTT") % 1000000007)
