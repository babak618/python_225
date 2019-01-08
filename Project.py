import csv
csv_file = open('sample.csv')
csv_read = csv.reader(csv_file)
for i in csv_read:
     print(i)


