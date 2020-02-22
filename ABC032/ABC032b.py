# ABC032b
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input()[:-1]
k = int(input())
password = set()

for i in range(len(s)-k+1):
    password.add(s[i:i+k])
print(len(password))
# len(password)
