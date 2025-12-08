class Car:
   def __init__(self, brand, model, year):
        self.brand = brand  # Object attribute
        self.model = model  # Object attribute
        self.year = year    # Object attribute
        
   def display_info(self):
       print(f"Car: {self.brand} {self.model}, Year: {self.year}")

   def __str__(self):
       return f"{self.brand} {self.model}"


car1 = Car('Fiat','Tipo',2024)
car2 = Car('Polonez','Karo',2003)
car1.display_info()
car2.display_info()
#lub
print(car1.brand) #prints only the brand
print(car1)
