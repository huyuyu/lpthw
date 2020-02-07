# Loops and Lists

import numpy

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

print("whole[the_count] : " , the_count)
print("whole[fruits] : " , fruits)
print("whole[change] : " , change)

# 输出列表内容
for number in the_count:
    print("This is count {}".format(number))

for fruit in fruits:
    print(f"This is fruit {fruit} ")

for i in change:
    print(f"I got {i}")

elements = []

# 给列表赋值
for i in range(0, 10):
    elements.append(i)

for element in elements:
    print("Element was : {}".format(element))

# Study Drills

testTwo = [0] * 5    # = testTwo[5]
print(testTwo)

# 创建num_list1[9][2], 并初始化为1
num_list1 = [ [1] * 2 for i in range(9)]
print(num_list1)

# 创建num_list2[2][5], 并初始化为0
num_list2 = numpy.zeros((2,5))
print(num_list2)

# 给二维数组赋值
for i in range(9):
    for j in range (2):
        num_list1[i][j] = i + j

for i in range(2):
    for j in range(5):
        num_list2[i][j] = i + j

# 读取二维列表的值
print(num_list2)
for j in range(5):
    print("num_list2[1][{j}] = ",num_list2[1][j])