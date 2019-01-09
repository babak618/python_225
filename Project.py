import csv
with open('sample.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    list1 = [row for row in csv_read]
    #print(list1)
    list2 = [column[5] for column in list1]
    #print(list2)
    print(max(list2))
    line = list2.index(max(list2))
    #print(line)
    print(list1[line])

