import math
a = int(input().replace(' ', ''))
print('Yes' if math.sqrt(a).is_integer() else 'No')
