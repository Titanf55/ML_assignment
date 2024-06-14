try:
 num=int(input("enter num"))
except TypeError:
  print('enter a number')

if num%2==0:
  print ('even')
else :
  print ('odd')        