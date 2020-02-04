# Reading Files

from sys import argv 

script, filename = argv
txt = open(filename)
print(f"Here is your file {filename} :")
print(txt.read())

print("Type the filename again :")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())

# Study Drills
# 打开后需要关闭文件；python不会组织你多次打开同一个文件
txt.close()
txt_again.close()