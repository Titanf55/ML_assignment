
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully!")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print("An error occurred:", e)


source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
print(copy_file(source_file, destination_file))