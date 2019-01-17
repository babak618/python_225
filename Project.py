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
# <date>[0],<OPEN>[1],<HIGH>[2],<LOW>[3],<CLOSE>[4],<VOL>[5]
def morning_star_candle(list):
    for i in list:
        date,open,close,high,low,vol = i[0],i[1],i[4],i[2],i[3],i[5]
        if(100 * (abs(open - close))) / open < 1 and (abs(open + close) / 2) * 1.02 < high:
            print(i)


morning_star_candle(final_list)
