# for num in range(0, 100):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

for num in range (1, 100):
    if num > 0:
        for i in range(1, num):
            if (num % i) == 0:
                break
        else:
            print(num)