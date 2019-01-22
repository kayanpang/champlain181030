import csv

row_counter = 1
unique_type_set = set()
europe_order = 0
total_unit_sold = 0

with open("7_-_100_Sales_Records.csv", 'rt') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:

        if row_counter != 1:
            unique_type_set.add(row[2])
            total_unit_sold += int(row[8])
            if row[0] == "Europe":
                europe_order += 1

        row_counter += 1

print("total amount of unit sold {0}".format(total_unit_sold))
print("total records from Europe {0}".format(europe_order))
print("")
print("Here is a list of unique item types:")
list_counter = 1
for x in unique_type:
    print(str(list_counter) + " " + x)
    list_counter += 1
