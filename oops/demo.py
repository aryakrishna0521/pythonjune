class student:
    # roll_no:int
    # name:str
    # age:int
    # gender:str
    # contact_no:str
    # address:str
  

    def __init__(self,roll_no,name,age,gender,contact_no,address):  #self for current object name,to point current instance

        self.roll_no=roll_no
        self.name=name         #initialize instance variable >constructor duty
        self.age=age        
        self.gender=gender
        self.contact_no=contact_no
        self.address=address

    def display_student(self):
        print(self.roll_no,self.name,self.age,self.gender,self.contact_no,self.address)

#creating object 

student_instance=student(1,"arya",20,"female","87654321","new york city")
# student_instance.set_student(1,"arya",20,"female","87654321","new york city")
student_instance.display_student()








# constructor
# python=__init__
# java=classname
# js-constructor