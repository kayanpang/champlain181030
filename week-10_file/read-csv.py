# this is actually write a csv
import csv
csv_data= [["StudentId", "Grade"], [123456, "A"]]
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csv_data)
