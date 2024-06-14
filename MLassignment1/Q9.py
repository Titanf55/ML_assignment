def check_substring(x, y):
    """Checks if a substring is present in a given string."""
    if y in x:
        return True
    else:
        return False

main_string = input("Enter the main string: ")
substring = input("Enter the substring to check for: ")

if check_substring(main_string, substring):
    print("The substring is present in the main string.")
else:
    print("The substring is not present in the main string.")
