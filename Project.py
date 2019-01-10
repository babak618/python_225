import csv
with open('SAIPA-Co.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    list1 = [row for row in csv_read]
    #print(list1)
    list2 = []
    for i in list1:
        if '<OPEN>' not in i:
            list2.append(i)
    #print(list2)
    list3 = [column[5] for column in list2]
    print(max(list3))
    line = list3.index(max(list3))
    #print(line)
    print(list2[line])

