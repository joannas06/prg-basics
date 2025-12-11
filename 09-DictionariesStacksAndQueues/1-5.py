countries = [
{"name":"Poland", "population":38000000},
{"name":"Japan", "population":120000000},
{"name":"USA", "population":4508793000},
{"name":"Brazil", "population":300000000},
{"name":"India", "population":10000000000}
]

print("COUNTRY  POPULATION")
for item in countries:
    for key,value in item.items():
        print(f'{value}', end="  ")
    print()