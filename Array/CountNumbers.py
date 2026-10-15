num = 58732858
count = 0

while num > 0:
    num = num // 10
    count += 1

print(count)

# Method 2

from math import *

def countDigits(num):
    return int(log10(num)+1)