from array import *

arr = array('i', [])
n = int(input("Enter the length of array: "))

for i in range(0, n):
    arr.append(int(input("Enter next input:")))


for x in arr:
    print(x, end=" ")