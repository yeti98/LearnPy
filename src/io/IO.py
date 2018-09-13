
from  sys import argv

script, filename = argv

pointer = open(filename, 'w') #you should notice this pointer
# w is called access mode. In further reading, reference here: https://www.tutorialspoint.com/python3/python_files_io.htm


one_line = pointer.readline() #read one line
one_line_limited = pointer.readline(2) # you can limit number of character will be readed
print(one_line_limited)
contents = pointer.read() #read all
print(contents)

pointer.truncate() # Trucate file, truncate() necessary with 'w' parameter

pointer.write("This is the first line of file\n")
pointer.write("And this a the second")


pointer.close() #similar to File->Save
