 
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


        
     
