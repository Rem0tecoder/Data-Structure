'''n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11

for num in n:
    hash_list[num]+=1

for num in m:
    if num < 0 or num > 10:
        print(0)
    else:
        print(hash_list[num])

print(hash_list[5])

# Dictionary

h_list = dict()
for num in n:
    h_list[num]+=1

for num in m:
    h_list[num]

print(h_list(2)) '''


# Character Hashing
s = "azyxyyyzaaaa"
q = ["d", "a", "y", "x"]
hash_list = [0]*26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index]+=1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
