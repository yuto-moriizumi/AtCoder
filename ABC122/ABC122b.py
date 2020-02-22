import re
cstr = input()
result = re.findall("[ACGT]+", cstr)
nums = [len(s) for s in result]
if not nums:
    nums = [0]
print(max(nums))
