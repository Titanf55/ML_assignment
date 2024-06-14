import csv

# Data to be written into the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# File path where you want to save the CSV file
csv_file_path = 'example15.csv'

# Writing data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print("CSV file created successfully!")


import csv

# File path of the CSV file
csv_file_path = 'example15.csv'

# Reading data from the CSV file
with open(csv_file_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(', '.join(row))
#It joins each element of the list together with a comma and a space between them.