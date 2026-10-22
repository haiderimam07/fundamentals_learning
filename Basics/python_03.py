# working with lists in python
# lists is mutbale
# lists_name=[] syntax
# what we can put inside  the lists string, number , boolean or anything
names=["haider", "Imam", "hello", 57]

print(names)
print(names[1])

# if we put negative we can acccess from the last 
# so simply if i said names[-1]
print(names[-1])
# it will print imam


# we can also specify range to print
print(names[1:3])

# fundtions in lists

my_numbers=[54,23,2,56,87,00]
# extend() 
names.extend(my_numbers)
print(names)

# some common functions of lists
# append() individual items in the list add the item in the end of the list
# insert(index,"value")
# remove()
# clear() empty the lists

# pop remove the last element of the lists
# index
print(names.index("imam"))
# count() count the number of occurences
# sort()
# reverse()
# copy
