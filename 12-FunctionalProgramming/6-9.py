dit = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positive_cities = filter(lambda city: dit[city] > 0, dit)

print("Cities wiht positive temp:"," ".join(positive_cities))