# Else and If

people = 30
cars = 40
trucks = 15

if cars > people:
	print("We should take the cars.") #
elif cars < people:
	print("We should not take the cars.") 
else:
	print("We can't decide.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.") #
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.") #
else:
	print("Fine, let's stay home then.")

if cars > people or trucks > cars :
    print("123") #
else:
    print("dddd")

# Study Drills

# 如果if中有多个代码块是正确的，则会从顶部开始，只运行第一个代码块