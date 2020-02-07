# While Loops

i=0 
numbers = []

while i < 6:
	# print(f"At the top i is {i}") 
	numbers.append(i)
	i=i+2
	print("Numbers now: ", numbers)
	# print(f"At the bottom i is {i}")

print("The numbers: ")
for num in numbers: 
	print(num)

# Study Drills

print(numbers)

test = []
for i in range(6):
    test.append(i)
    print("test now: ", test)

# for循环和while循环有什么区别？
#   for循环只能迭代（循环）“覆盖”事物集合。
#   while循环可以执行任何类型的迭代（循环）。