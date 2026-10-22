# read from external file like .txt or html or anyhting

# steps
# open (in modes - r:read, w:write ,a:append, r+:read and write) ->  do things you want ->close file


name_file=open("C:/Users/haide/Work/python_learning/Basics/file.txt","r")
if name_file.readable():
    print(name_file.read())
name_file.close()

name_file=open("C:/Users/haide/Work/python_learning/Basics/file.txt","r")
if name_file.readable():
    print(name_file.readline())
name_file.close()

name_file=open("C:/Users/haide/Work/python_learning/Basics/file.txt","r")
if name_file.readable():
    print(name_file.readlines())
name_file.close()

name_file=open("C:/Users/haide/Work/python_learning/Basics/file.txt","a")
name_file.write(" line added in the last via append ")
name_file.close()

name_file=open("C:/Users/haide/Work/python_learning/Basics/file2.txt","w")
# this will rep;ace all the text and replace this fron this text
name_file.write(" line added in the last via append ")
name_file.close()
