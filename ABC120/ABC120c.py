s = input()

slength = len(s)
for _ in range(5000):
    s = s.replace("01", "").replace("10", "")
print(slength-len(s))
