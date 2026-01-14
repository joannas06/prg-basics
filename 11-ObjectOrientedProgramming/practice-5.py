import random
class Thermometer:
    def __init__(self,):
        temp = round(random.uniform(36,42),1)
        self.temp = temp
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def checktemp(self):
        if self.is_on:
            print("The thermometer is on!")
            print("Checking temperature...")
            print(f"Your temperature is: {self.temp}")
            if self.temp <= 37:
                print("Your temperature is normal :)")
            elif self.temp >37 and self.temp < 41:
                print("You have a fever :(")
            elif self.temp >= 41:
                print("Critical temperature! Go to hospital")
        else:
            print("The thermometer is off!")


def main():
    checking = Thermometer()
    checking.turn_on()
    checking.checktemp()
    checking.turn_off()
    checking.checktemp()

if __name__ == "__main__":
    main()