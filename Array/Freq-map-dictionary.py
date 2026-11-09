# Method 1
from math import *
nums = [5,6,5,7,8,9,0,1,1,5,5,68,0,9]
f = dict()

for i in range(0,len(nums)):
    if nums[i] in f:
        f[nums[i]]+=1
    else:
        f[nums[i]]=1

print(f[5])

# Method 2

nums = [5,6,5,7,8,9,0,1,1,5,5,68,0,9]
h = {}

n = len(nums)
for i in range(0,n):
    h[nums[i]] = h.get(nums[i],0)+1

print(h[68])