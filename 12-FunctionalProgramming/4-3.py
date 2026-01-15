grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

average = sum(list(filter(lambda x: x>2,grades)))
how_many = len(list(filter(lambda y: y>2,grades)))

print(average/how_many)