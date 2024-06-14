list1=list(input("enter items in list"))
print(list1)



def num_list(list1):
 number_list = [int(char) for char in list1]  # Convert each char back to int and create a list
 return number_list

print(num_list(list1))
numbers_list = num_list(list1)

print("Minimum value:",  min(numbers_list))
print("Maximum value:",  max(numbers_list))

