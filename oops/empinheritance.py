class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(self.name,self.age,self.gender)


class Employee(Person):
    def __init__(self,name,age,gender,eid,department,salary):
        super().__init__(name,age,gender)

        self.eid=eid
        self.department=department
        self.salary=salary
        
    def display(self):
        super().display()
        print(self.eid,self.department,self.salary)

Employee_instance=Employee("arya",20,"f",123,"sales",65444)
Employee_instance.display()
    