sen=input("enter sentence ")

length = len(sen)
sen=sen.upper()

frequency = {}
for char in sen:
        if char in frequency:
            frequency[char] += 1  # dict1['key1'] = 'value1' + 1
        else:
            frequency[char] = 1
       

for char, freq in frequency.items():
    print(f"'{char}': {freq}")

  