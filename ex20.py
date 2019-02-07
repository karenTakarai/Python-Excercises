from sys import argv

#Unpack the arguments
script, input_file = argv

#Create a function which print the content of a file that has been pass as argument
def print_all(f):
    print(f.read())

#Create a function to set the pointer to the start of the file
def rewind(f):
    f.seek(0)

#Create a function too print the line count variable, and the current line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#create a file object of the file located on the path specified in input_file variable.
current_file = open(input_file)

print("First let's print the whole file:\n")

#call the function print all and print the all content of the file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#call the function rewind and rewind the pointer to the start of the file
rewind(current_file)

print("Let's print three lines:")

#add 1 to the lines counter and call the function to print the current line (line 1), passing as arguments the...
#line counter and the file
current_line = 1
print_a_line(current_line, current_file)

#add 1 to the lines counter and call the function to print the current line (line 2), passing as arguments the...
#line counter and the file
current_line += 1
print_a_line(current_line, current_file)

#add 1 to the lines counter and call the function to print the current line (line 3), passing as arguments the...
#line counter and the file
current_line += 1
print_a_line(current_line, current_file)