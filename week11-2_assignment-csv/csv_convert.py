import csv

row_counter = 1
csv_data = [["Name","Sex","Age","Height (cm)","Weight (kg)"]]

with open("biostats2.csv", 'rt') as Bio_stat:
    reader = csv.reader(Bio_stat)
    for row in reader:
        if row_counter != 1:

            row[3] = float(row[3]) * 2.54
            row[4] = float(row[4]) * 0.454
        row_counter += 1
        csv_data.append(row)


with open("convert.csv", 'w', newline='') as Convert_unit:
    writer = csv.writer(Convert_unit)
    writer.writerows(csv_data)