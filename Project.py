import csv
import re
final_list = []
with open('SAIPA-Co.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        list1 = [float(i) for i in row if re.match("\d", i)]
        if len(list1) > 0:
            final_list.append(list1)

print(final_list)