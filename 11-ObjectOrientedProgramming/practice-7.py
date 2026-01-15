class Statistics:
    def __init__(self):
        self.array = []
        self.max = 0
        self.min = 9999999
        self.meaan = 0
    def add_to_array(self):
        while True:
            user_input = input("Enter a number, type 'stop' to stop: ")
            
            if user_input.lower() == 'stop':
                break
            
            try:
                number = int(user_input)
                self.array.append(number)
            except ValueError:
                print("Invalid input! Please enter a whole number or 'stop'.")
    def greatest(self):
        for i in self.array:
            if i>self.max:
                self.max = i
    def smallest(self):
        for i in self.array:
            if i < self.min:
                self.min = i
    def meann(self):
        how_many = len(self.array)
        sum = 0
        for i in self.array:
            sum += i
        
        self.meaan = sum/how_many

    def showinfo(self):
        print("The array: ")
        print(*self.array)
        print(f"The greatest number in the array is: {self.max}")
        print(f"The smallest number in the array is {self.min}")
        print(f"The arithmetic mean is: {self.meaan}")


def main():
    math = Statistics()
    math.add_to_array()
    math.showinfo()
    math.greatest()
    math.smallest()
    math.meann()
    math.showinfo()

if __name__ == "__main__":
    main()