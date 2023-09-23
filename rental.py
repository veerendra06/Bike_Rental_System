########   BIKE RENTAL SYSTEM
class Bikeshop():
    def __init__(self,stock):
        self.stock =stock
    def display(self):
        print(self.stock)   
           
    def rant_bike(self,q):
        
        if q <= 0:
            print("pls enter positive value ")
        elif q > self.stock:
            print(" enter value less then stock")
        else:
            self.stock = self.stock - q
            print("total price" ,q*100)
            print ("total stock", self.stock)
       
while True:
    obj = Bikeshop(100)
    
    vr = int(input('''
          
     1   Display stock
     2   Rent a bike
     3   exit       
          1
                   
          '''))
    
    if vr == 1:  
        obj.display()
        
    elif vr == 2:
        n = int(input("Enter the Quanatity : "))
        obj.rant_bike(n)
        
    else:
        break
        
    

