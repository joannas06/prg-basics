# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]
n = 0
amount_together = 0
for i in product_prices:
    amount_together += i * product_quantities[n]
    n+=1

print(f'{amount_together:.2f}')
