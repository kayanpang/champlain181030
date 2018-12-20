import datetime

x = datetime.datetime.now()
print(x)

print(x.strftime("%Y-%m"))

date_to_print = ""
date_to_print += x.strftime("%Y-%m")
date_to_print += x.strftime("%p").lower()
date_to_print += x.strftime("%Y-%m-%d %I:%M%p").lower()

print(x.strftime("%Y-%m-%d %I:%M%p").lower())