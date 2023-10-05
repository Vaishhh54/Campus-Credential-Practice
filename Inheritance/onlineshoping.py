from abc import abstractmethod


class Product:
    def __init__(self):
        self.name = ""
        self.price = 0.0
    @abstractmethod
    def get_price(self):
        pass
    @abstractmethod
    def display_details(self):
        pass
class Electronics(Product):
    def __init__(self):
        self.brand = ""
        self.warranty =""
        self.name = input("Enter Name of product: ")
        self.price = int(input("Enter price of Product: "))
        self.brand = input("Enter Brand of Prize: ")
        self.warranty = input("Enter warranty of product")
    def get_price(self):
       return self.brand,self.warranty
      
    def display_details(self):
        print("Product Name is: ",self.name)
        print("product price is : ",self.price)
        print("Product brand is: ",self.brand)    
class Clothing(Product):
    def __init__(self,size,color,material):
        self.size =size
        self.color = color
        self.material = material
class Books(Product):
    def __init__(self,author,genre):
        self.author =author
        self.genre = genre
    def get_price(self):
        pass
    def display_details(self):
        pass

s = Electronics()
s.get_price()
s.display_details()
