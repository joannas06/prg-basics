class Bank:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.balance = balance
    def withdraw(self,amtw):
        if amtw <= self.balance:
            self.balance -= amtw
        else:
            print("Insufficient funds!")
    def deposit(self,amtd):
        self.balance += amtd
    def showinfo(self):
        print(f"Bank account: {self.account_no[0:2]} {self.account_no[2:6]} {self.account_no[6:10]} {self.account_no[10:14]} {self.account_no[14:18]} {self.account_no[18:22]} {self.account_no[22:26]}")
        print(f"Balance: PLN {self.balance}")


def main():
    myaccount = Bank("12345655559090111100007722",1200.78)
    myaccount.showinfo()
    myaccount.deposit(25.30)
    myaccount.showinfo()
    myaccount.withdraw(31.70)
    myaccount.showinfo()
    myaccount.withdraw(14)
    myaccount.showinfo()

if __name__ == "__main__":
    main()