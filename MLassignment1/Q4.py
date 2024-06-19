 
# name = int(input('Enter name: '))
# if isinstance(name, str):
#     print('Hola', name ,'como estas')

# else:
#     while True:
#         print('Invalid input. Please enter a string.')
#         name = int(input('Enter name: '))
#         if isinstance(name, str):
#             print('Hola', name ,'como estas')
# 
#             break
try:
 name=int(input("enter name"))
except (TypeError ,ValueError):
  print('hola como estas')
 #all these will produce errors _ _ _ _ _ _ _ _ _ _  
                                 #enter atleat 2 charac like enter 12k3j output kj 
import re

def get_alpha_string(prompt):
    while True:
        user_input = input(prompt)
        # Use regular expression to match only alphabetic characters
        alpha_string = re.sub(r'[^a-zA-Z]', '', user_input)
        
        if len(alpha_string) >= 2:
            return alpha_string
        else:
            print("Please enter at least 2 letter name.")

                                  #enter 12k3j output kj
# def get_alpha_string(prompt):
#     while True:
#         user_input = input(prompt)
#         alpha_string = ''.join(filter(str.isalpha, user_input))  # Filter out non-alphabetic characters
        
#         if len(alpha_string) >= 2:
#             return alpha_string
#         else:
#             print("Please enter at least two alphabetic characters.")

                                  #enter 12k3j it will take if has atleast 2 charc
# def get_alpha_string(prompt):
#     while True:
#         user_input = input(prompt)
#         alpha_count = sum(1 for char in user_input if char.isalpha())
        
#         if alpha_count >= 2:
#             return user_input
#         else:
#             print("Please enter a string with at least two alphabetic characters.")

alpha_string = get_alpha_string("Enter a string with only alphabetic characters: ")
print(f"hola {alpha_string} como estas!")


        
     
