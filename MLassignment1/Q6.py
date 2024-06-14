file_name = input("enter file name")

try:
    with open(file_name, "r") as file:
        
        content = file.read()
        
        print("Content of", file_name, ":\n", content)
except FileNotFoundError:
    print("File not found. Please make sure the file exists and try again.")
except Exception as e:
    print("An error occurred:", e)
