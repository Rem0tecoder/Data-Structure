'''n = 10
val = []
for i in range(0,n):
    n = int(input("Enter an Array: "))
    val.append(n)

for i in range(len(val)):
    print(val[i])


for i in range(1, n+1):
    for j in range(1, n+1):
        print('Hello') '''



# Count total numbers of factors
from math import sqrt
num = 36
result = []
count = 0
sum = 0

for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        count+=1
        if num // i != i:
            result.append(num // i)
            count +=1
            

result.sort()
print(result)
print(count)
