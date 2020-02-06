# More Variables and Printing

my_name = "Zed A. Shaw"
my_age = 35
my_height = 74
my_weight = 180 
my_eyes = "Black"
my_teeth = 'White'
my_hair = "Black"
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")

# Study Drills
# 将英寸转换成厘米
inches = 2.54
print(f"He's  {'%.2f' % float(my_height/inches)} centimetres tall.")

# 将磅转换成公斤
pounds = 0.45
print(f"He's {'%.2f' % float(my_weight * pounds)} pounds heavy.")

# 使用round进行浮点数的舍入？
print(round(1.733333,2))