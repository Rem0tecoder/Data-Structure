num = 1634
nod = len(str(num))
result = 0

while num > 0:
    last_digit = num % 10
    result = result + last_digit **nod
    num = num //10

print(result)