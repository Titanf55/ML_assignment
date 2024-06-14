# TO WRITE IN A FILE
inp = input("Enter a string: ")
with open("file5.txt", "w") as file:
    file.write(inp)
print("String has been written to file5.txt")
inp2 = input("Enter a string at beginning: ")
with open("file5.txt", "r+") as file:
        content = file.read()
        file.seek(0, 0)  
        file.write(inp2 + "\n" + content)


def append_after_word(file_path, target_word, data):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            file.write(line)
            if target_word in line:
                file.write(data + "\n")

file_path = "file5.txt"
target_word = "Hola"
data_to_append = "New data after 'hola'"
append_after_word(file_path, target_word, data_to_append)

def append_to_line(file_path, line_number, data):
    with open(file_path, "r") as file:
        lines = file.readlines()

    lines.insert(line_number - 1, data + "\n") 

    with open(file_path, "w") as file:
        file.writelines(lines)

file_path = "file5.txt"
line_number = 3  
data_to_append = "New data at line 3"
append_to_line(file_path, line_number, data_to_append)






