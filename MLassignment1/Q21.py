list1=list(input("enter items in list"))
print(list1)

frequency = {}
for char in list1:
        if char in frequency:
            frequency[char] += 1  # dict1['key1'] = 'value1'
        else:
            frequency[char] = 1
       

print(frequency)


