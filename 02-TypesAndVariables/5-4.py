## Amount : 13.56
# VAT 23% :  3.64

price = input('Price of product ')
price_float = float(price)

amount = price_float - price_float*0.23

VAT = price_float * 0.23

print(f'The original price was: {price_float}')
print(f'The amount is: {amount: .2f}')
print(f'The VAT is: {VAT: .2f}')