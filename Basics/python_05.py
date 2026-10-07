# funcitions in python
# indentation is very important instead of curly braces we use indentation
# syntax


# defination of function
def say_hi(name,age):
    print("hello"+ name , "I am ",age, "years old")

# calling funciton

my="haider"
age=8
say_hi(my, age)

def power_num(base, power):
    ans=1
    while(power>0):
        ans=base*ans
        power=power-1

    return ans    

value=power_num(2,5)
print(value)

# if else elif
# syntax

age=9

if age>9:
    print(age)
elif age<9:
    print("age is greater than or equal to 9")
else:
    print("fuck off")


# conditional statements and or not by simply usng the word

ismale=True
isfemale=False

if ismale or isfemale:
    print("gay")
else:
    print("not gay")

name="hairder"
if (name=="haider"):
    print("yes")
elif name=="hairder":
    print("no")
