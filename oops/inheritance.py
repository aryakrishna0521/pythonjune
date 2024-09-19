class Vehicle:
    def start(self):
        print("vehicle starting method")
    def accelarate(self):
        print("vehicle accelarate method") 


class swift(Vehicle):
    pass 
swift_instance=swift()
swift_instance.accelarate()  
swift_instance.start()       