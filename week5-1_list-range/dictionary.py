# dictionary for provinces
provinces_list = {'QC': 'Quebec', 'ON': 'Ontario', 'BC': 'British Columbia'}
Prov = input("Enter the province code > ")
result = provinces_list[Prov.upper()]
# it will convert the input to upper case no matter what the users input
print("The province name is {0}".format(result))
# use operation to prevent crash when user entry that does not exist in the list/dictionary (ex.: MN)
