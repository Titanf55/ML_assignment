numbers_str=input("enter numbers with spaces")
print(numbers_str)

numbers_str= numbers_str.split()

numbers_list=[]
# Convert the list of strings to a list of integers
try:
    numbers_list = [int(num) for num in numbers_str]    
except ValueError:
    print("Please enter valid integers separated by spaces.")
print(numbers_list)
sum=0
for i in numbers_list:
    sum+=i
print(sum)
