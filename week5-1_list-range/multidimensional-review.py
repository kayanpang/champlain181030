# hard code way
car_inspects = [[1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]]
for car in car_inspects:
    print(car)
# 2nd way
car_inspects = [[1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]]
count = 0
for car in car_inspects:
    count += 1
    print("inspection for car number " + str(count))
    print(car)
# print the list of inspectors
car_inspects = [[1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]]
count = 0
for car in car_inspects:
    count += 1
    print("inspection for car number " + str(count))
    print("Inspector 1 : " + str(car[0]))
    print("Inspector 2 : " + str(car[1]))
    print("Inspector 3 : " + str(car[2]))