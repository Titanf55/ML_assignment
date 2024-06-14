try:
 digits=int(input("enter num"))
except (TypeError ,ValueError):
  print('enter a number')

number_list=[] 

digits = abs(digits)

def is_num(digits):
    
 number_str = str(digits)  # Convert number to string
 number_list = [int(char) for char in number_str]  # Convert each char back to int and create a list
 print(number_list)
 return number_list

number_list = is_num(digits)   
  
sum=0
for i in number_list :
 sum += i
 
print(sum)  
   

   
