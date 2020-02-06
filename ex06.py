# Strings and Text

types_of_people = 10
binary = "binary"
do_not = "don't"
x = f"There are {types_of_people} types of people."
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said : {x}")
print(f"I also said : '{y}'")

# 给带有参数的字符串赋值 str.format("str1","str2", ... )
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} and {}"
print(joke_evaluation.format(hilarious,"test"))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)