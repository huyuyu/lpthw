# Functions and Files

from sys import argv
script, input_file = argv
current_file = open(input_file)

def print_all(f): 
    print(f.read())

def rewind(f): 
    f.seek(0)

def print_a_line(line_count, f): 
    print(line_count, f.readline())

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.") 
rewind(current_file)

print("Let's print three lines:") 
current_line = 3
print_a_line(current_line, current_file) #  每次都从光标所在处为第一行算起

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# Study Drills

