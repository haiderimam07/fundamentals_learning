# inheritance in python
from python_11 import chef

# let say the chinese checf can do all those things that a normla checf can do so instead of writing all the class again we can simply inherit the properties from the chef class
class chineseChef(chef):
    # we can also override some funcitonality accroidng to the need
    # replaced inherited funciton
    def make_special_dish(self):
        print("chinese chef specailty is haaka noodles")

    # native function 
    def make_fried_rice(self):
        print("chinese make fried rice")


# object creation
mychinesechef=chineseChef()

# calling the object funciton 
# this function is inherited frm the chef class
mychinesechef.make_special_dish()