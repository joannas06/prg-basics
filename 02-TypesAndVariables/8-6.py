###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#

distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption (liters/100km): '))

# Calculate total fuel needed
# Formula: (distance / 100) * consumption
total_fuel_consumption = (distance * fuel_consumption) / 100

# Calculate total cost
total_cost = total_fuel_consumption * fuel_price

print(f'Total fuel consumption: {total_fuel_consumption} liters')
print(f'Total transport cost: {total_cost}')