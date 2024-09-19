class Grandparent:
    def m1(self):
        print("grandparent class m1 method ")

class Parent:
    def m2(self):
        print("parent classs m2 method")

class Child(Parent,Grandparent):
    def m3(self):
        print("child class m3 method")

Child_instance=Child()
Child_instance.m3()
Child_instance.m2()
Child_instance.m1()
    