def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

string1 = "Astronomer"
string2 = "Moon starer"

if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams of each other.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")
