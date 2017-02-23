import csv
 with open(‘my_input_file.csv’, ‘r’) as f:
my_reader = csv.reader(f)
data = list(my_reader)
