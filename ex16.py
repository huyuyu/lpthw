# Reading and Writing Files

# readline : Read just one line 
# truncate : empties the File
# write(" ") : 写入
# seek(0) : 将光标移动到文首


from sys import argv
script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()  # 清空
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3 + "\n")
# target.write("\n")


# Study Drills

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.write(f"{line1} \n {line2} \n {line3} \n")
print("And finally, we close it.")
target.close()


