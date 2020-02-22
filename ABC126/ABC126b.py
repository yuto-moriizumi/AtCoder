import sys
input = sys.stdin.readline

s = input()
isMaeMM = False
if (0 < int(s[0:2]) < 13):

    isMaeMM = True
isUshiroMM = False
if (0 < int(s[2:]) < 13):

    isUshiroMM = True
if (isMaeMM):
    if (isUshiroMM):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if (isUshiroMM):
        print("YYMM")
    else:
        print("NA")
