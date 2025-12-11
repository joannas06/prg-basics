price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print('Before discount')
for key,value in price_list.items():
    print(f'{key} {value}')

totalbd = 0
for key,value in price_list.items():
    totalbd += value
print(f'Total before discount:{totalbd:.2f}')
value2 =0
totalad = 0
for key,value in price_list.items():
    value2 = value * 0.9
    totalad += value2
    print(f'Values after discount: {key}:{value2:.2f}')
    print(f'Total value after discount: {totalad:.2f}')
