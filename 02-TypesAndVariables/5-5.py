# Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
 #Reduction: 3.71

price = input('The original price is: ')
price_float = float(price)
discounted_price = price_float * 0.85
deducted_price = price_float * 0.15

print(f'The original price was: {price_float}')
print(f'The discount is 15%')
print(f'The dicounted price is: {discounted_price: .2f}')
print(f'The amount deducted is: {deducted_price: .2f}')