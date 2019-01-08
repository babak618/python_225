import csv
with open('sample.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    for i in csv_read:
        print(i)
