class book:
    # title:str
    # author:str
    # price:int
    # language:str


    def __init__(self,title,author,price,language):
        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_book(self):
         print(self.title,self.author,self.price,self.language)


    def __str__(self):
        return  self.title    

book_instance1=book("alchemist","paulo koylo",290,"english")  
book_instance2=book("one indian girl","chethan bagat",250,"english") 
book_instance1.display_book() 
print(book_instance1)    
