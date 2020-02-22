#最初に入れておくとinputが早くなる
import sys
input = sys.stdin.readline

s = input()
flag = False

for i in range(1, len(s)):
    if (s[i] == s[i - 1]):
        flag = True

if (flag):
    print("Bad")
    exit()
print("Good")