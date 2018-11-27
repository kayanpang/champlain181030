# use operation to prevent crash when user entry that does not exist in the list/dictionary (ex.: MN)
provinces_list = {'QC': 'Quebec', 'ON': 'Ontario', 'BC': 'British Columbia'}
Prov = input("Enter the province code > ")
if Prov.upper() not in provinces_list:
    print("Sorry the province code is not recognized!")
else:
    result = provinces_list[Prov.upper()]
    print("The province name is {0}".format(result))
