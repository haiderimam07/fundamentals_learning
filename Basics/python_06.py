# dictionary are the special type of data structure in python which allowed use to store data in key value pair
# it is mutable
# syntax of writing it

dictionary_name={
    "name":"haider",
    "age": 34,
    "number":"9311057265"
}
dictionary_name["age"]=76
print(dictionary_name)
print(dictionary_name["age"])

# some funcitons
# get() it can find the value of this key and we can pass a default value if value is not find 
print(dictionary_name.get("loc", "location not found"))


# for loop
text="haiderimam"
for i in text:
    print(i)

for object in dictionary_name.values():
    
    print(object)


for i in range(3,8):
    print(i)

# print(dictionary_name[0])
for i in range(len(dictionary_name)):
    print(i)

for key in dictionary_name:
    print(dictionary_name[key])


for key, value in dictionary_name.items():
    print(f"{key}: {value}")