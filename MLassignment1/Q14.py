lines = []

print("Enter multiple lines of input. Press Enter on an empty line to stop.")

# Continue reading input until an empty line is entered
while True:
    line = input()
    if not line:  # If the line is empty, break out of the loop
        break
    lines.append(line)

# Print all the lines entered by the user
print("You entered:")
for line in lines:
    print(line)
