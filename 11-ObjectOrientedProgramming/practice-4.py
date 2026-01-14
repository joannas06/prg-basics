class EBOOK:
    def __init__(self,title,author,pages,current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def read(self,no):
        if self.is_open:
            self.current_page += no
        else:
            print("Error! the book is closed")
    def showinfo(self):
        print(f"The book is: {self.title}, written by: {self.author}, it has: {self.pages} pages.")
        if self.is_open:
            print(f"The book is open, you are on page: {self.current_page}")
        else:
            print(f"The book is closed")

def main():
    ebook = EBOOK("Hunger games","Suzanne Collins",321,1)
    ebook.open()
    ebook.showinfo()
    ebook.read(10)
    ebook.showinfo()
    ebook.close()
    ebook.showinfo()
    ebook.read(10)
    ebook.showinfo()
if __name__ == "__main__":
    main()