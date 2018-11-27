# another method: except
provinces_list = {'QC': 'Quebec', 'ON': 'Ontario', 'BC': 'British Columbia'}
Prov = input("Enter the province code > ")
try:
    result = provinces_list[Prov.upper()]
    print("The province name is {0}".format(result))
except KeyError:
    print("Sorry the province code is not recognized!")