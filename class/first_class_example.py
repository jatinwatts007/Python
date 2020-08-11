class book():
    types="motivation"
    def __init__(self,name,pages):
        self.pages = pages
        self.name = name
    def show_book(self,name):
        self.name = name
        print(self.name)
        print(self.pages)
