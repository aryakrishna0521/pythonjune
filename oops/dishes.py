class dish:
    item:str
    price:int
    quantity:str

    def __init__(self,item,price,quantity):
        self.item=item
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return self.item


class restorant:
    
    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.dishes=[]
    
    def add_item(self,dish):
        self.dishes.append(self.dishes)
    def list_dishes(self):
        for b in self.dishes:
         print(b)

mandi_instance=dish("mandi","200","half")
porotta_instance=dish("porotta","20","3")
biriyani_instance=dish("biriyani","150","1")

restorant_instance=restorant("galaxy","kakkanad")
restorant_instance.add_item(mandi_instance)
restorant_instance.add_item(porotta_instance)
restorant_instance.dishe()

        