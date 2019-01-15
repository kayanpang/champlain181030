import csv
with open("person.csv", "rt") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
        print(row[1])