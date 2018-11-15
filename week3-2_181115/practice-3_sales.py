# 3 sales
sale = "1.40"
sale2 = "2.30"
total = "The total sale price is "
sum = float(sale) + float(sale2)
print(total + str(sum))

# 3 Brendon
import decimal
sale = "1.40"
sale2 = "2.30"
sale_dec1 = decimal.Decimal(sale)
sale_dec2 = decimal.Decimal(sale2)

print(sale_dec1 + sale_dec2)