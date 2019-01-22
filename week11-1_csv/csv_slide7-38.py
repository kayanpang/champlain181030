import csv

with open("7_-_100_Sales_Records.csv", 'rt') as csv:
    reader = csv.reader(f)
    counter = 1
        for row in reader:
            if row[0] == "Europe":
        counter += 1

