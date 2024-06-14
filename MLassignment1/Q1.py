try:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1 + num2

    # Printing the sum
    print("The sum is", sum)

except ValueError:
    print("Please enter valid numbers.")


