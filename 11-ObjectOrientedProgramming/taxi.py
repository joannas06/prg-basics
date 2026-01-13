class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Distance: {self.distance}km, rate per kilometer: {self.rate_per_km}$ fare: {self.fare}')


def main():
    # your program
   ride1 = TaxiRide(3)
   ride2 = TaxiRide(2)
   ride1.calculate_fare(20)
   ride2.calculate_fare(10)
   ride1.print_receipt()
   ride2.print_receipt()



if __name__ == "__main__":
    main()
