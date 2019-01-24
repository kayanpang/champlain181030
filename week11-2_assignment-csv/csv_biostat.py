import csv

row_counter = 1
Age = 0
Lines = 0
Female = 0
Convert_cm = 0

with open("biostats2.csv", 'rt') as Bio_stat:
    reader = csv.reader(Bio_stat)
    for row in reader:
        if row_counter != 1:
            Age += int(row[2])
            Lines += 1
            if row[1] == "F":
                Female += 1

        row_counter += 1
    Average = Age / Lines
    Percentage = Female / Lines
    Male_percentage = float(1) - Percentage
    # double check Male_percentage



print(Age)
print(Lines)
print(Average)
print(Female)
print(Percentage)
print(Male_percentage)