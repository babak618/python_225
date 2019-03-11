import csv
import re
fs = []
with open('SIPA1-a.csv') as csv_file:
    csv_read = csv.reader(csv_file)
    for row in csv_read:
        list1 = [float(i) for i in row if re.match("\d", i)]
        if len(list1) > 0 and list1 not in fs:
            fs.append(list1)


# <date>[0],<OPEN>[1],<HIGH>[2],<LOW>[3],<CLOSE>[4],<VOL>[5]


def morning_star_candle(final_list):
    for i in final_list:
        date, open, close, high, low, vol = i[0], i[1], i[4], i[2], i[3], i[5]

        if (100 * (abs(open - close))) / open < 1 and (abs(open + close) / 2) * 1.01 < high:
            candle_index = fs.index(i)
            p_candle, n_candle = candle_index - 1, candle_index + 1  # previous candle, next candle

            if fs[p_candle][1] > fs[p_candle][4] and fs[p_candle][4] > low:  # previously candle structure

                if fs[n_candle][1] < fs[n_candle][4] and fs[n_candle][4] > fs[p_candle][4]:

                    if fs[n_candle][1] > (open and close):

                        if fs[n_candle][4] > ((fs[p_candle][1] - fs[p_candle][4]) / 2 ) + fs[p_candle][4]:

                            m = (str(i[0]))
                            print(f"{m[0:4]}--{m[4:6]}--{m[6:8]}")


morning_star_candle(fs)
print(len(fs))
