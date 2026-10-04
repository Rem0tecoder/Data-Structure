from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

for i in range(0, len(val)):

    print(val[i], end=" ")

print('\n')
for x in val:
    print(x, end=" ")

print(val.typecode)
val.reverse()

for i in range(0, len(val)):
    print(val[i], end=" ")

print('\n')


val.insert(3, 69)
val.append(100)
val[2] = 200

copyArray = array(val.typecode, (x*2 for x in val))
copyArray.pop(2)
copyArray.remove(138)

for i in range(0, len(copyArray)):
    print(copyArray[i], end=" ")