class Phone():
    def __init__(self,brand,color,owner):
        self.brand = brand
        self.color = color
        self.owner = owner
        self.is_charging = False
        self.is_on = False
        self.battery = 1

    def chargeyes(self):
        self.is_charging = True
    def chargeno(self):
        self.is_charging = False

    def batterynow(self,batterylife):
        self.battery=batterylife

    def onyes(self):
        self.is_on = True
    def onno(self):
        self.is_on = False

    def infodisplay(self):
        print(f'The brand of the phone is: {self.brand}')
        print(f'The color of the phone is: {self.color}')
        print(f'The owner of the phone is: {self.owner}')
        if self.is_charging:
            print(f'The phone is charging now, the battery is at: {self.battery}%')
        else:
            print(f'The phone is not charging, the batter is at: {self.battery}%')
        if self.is_on:
            print(f'The phone is on')
        else:
            print(f'The phone is off')

def main():
    myphone = Phone("Apple","Black","Joanna")
    myphone.chargeyes()
    myphone.batterynow(56)
    myphone.onno()
    myphone.infodisplay()

if __name__ == "__main__":
    main()

    

        


