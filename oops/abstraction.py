#hiding implementation detaills

from abc import ABC,abstractmethod
class Car(ABC):
    
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def  stop(self):
        pass

class Swift(Car):
    def start(self):
        print("car start")

    def accelerate(self):
        print("car accelarate")

    def stop(self):
        print("car stops") 

Car_instance=Swift()
Car_instance.start()  
Car_instance.accelerate()
Car_instance.stop()   