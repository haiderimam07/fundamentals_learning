# classes and objects in python

class Student:
    # initializer
    def __init__(self,name, age, branch, cgpa, has_back):
        self.name=name
        self.age=age
        self.branch=branch
        self.cgpa=cgpa
        self.has_back=has_back

    def is_passed(self):
        if self.has_back:
            return True
        else:
            return False

# object is the actual info of the student

student_haider=Student("haider", 23, "ECE", 7.7, False)
print(student_haider.name)
print(student_haider.is_passed())




# class functions
# functions tat are defied in the class that can be used in the class itself 


# inheritance in  python
class chef:
    def make_chicken(self):
        print("the chef makes a chicken")

    def make_salad(self):
        print("the chef makes a salad")

    def make_special_dish(self):
        print("special menu is tandoori chicken")