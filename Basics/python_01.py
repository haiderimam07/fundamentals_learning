print("writing from the terminal")

# variable and datatypes in python 
# string, number, boolean, 

character_name= "haider"
print("character_name is",character_name)

# cancatenation :adding two strngs
surname="Imam"
print(character_name + surname)

# convert any string in upper case or lower case
char_upper=surname.upper()
print(char_upper)

# lower case

char_lower= surname.lower()
print(char_lower)

# chec if the string is upper case or lower case or not

is_char_upper=surname.isupper()
print(is_char_upper)

# we can use multiple function one after another

print(surname.lower().isupper())

length_surname=len(surname)

# in order to simply point one character of the string we

first_letter=surname[0]
print(first_letter)

# we can simply get the index of any letter or start of the string
print(surname.index("am"))

# replcae any character or string 
print(surname.replace("Im", "ha"))


# numbers 

my_num=5
print(my_num)
# we can not cancatenate string to number so basically we can not do 5+"haider" it will give error
# convert number into string
print(str(my_num))

this_nums=-5
print(abs(this_nums))

# pow function power same as c++
print(pow(2,5))
# round() to round up decimal values

