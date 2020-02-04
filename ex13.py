# Parameters, Unpacking, Variables

from sys import argv  # 通过command line 传入参数变量
# 在cmd输入命令的时候为：python ex13.py arg1 arg2 arg3;需要将参数传入
script, first, second, third = argv
# 获取 argv 中的任何内容，然后按顺序将其分配给左边的所有变量。

print("The script is called:", script)      # ex13.py
print("Your first variable is:", first)     # arg1
print("Your second variable is:", second)   # arg2
print("Your third variable is:", third)     # arg3


# Study Drills
print("""
!!!What’s the difference between argv and input()? 
\tThe difference has to do with where the user is required to give input. If they give your script inputs on the command line, then you use argv. If you want them to input using the keyboard while the script is running, then use input().
""")
x = input('? ') 
print(x)