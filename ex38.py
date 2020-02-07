# Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar" 
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee","Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop的是最后一个员工
    print("Adding: ", next_one) 
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff) 
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])

# 将列表转换成字符串
print(' '.join(stuff)) 

# 将第三个和第四个员工用'#'号连接起来
print('#'.join(stuff[3:5])) 

# Study Drills

