# What Was That?
"""
ways to makea string goes across multiple lines :
   1. use \n
   2. use """   """
"""

print("I am 6'2\" tall." )  #如果不使用\，会出现语法错误
print('I am 6\'2" tall.')

tabby_cat = "\tI'm tabbed in ."
persian_cat = "I'm split \n on a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass

"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("aaaa \f aaa")
print("aaaa \r aaa")

#   \\ : Backslash (\)  
#   \' : Single-quote (')  
#   \" : Double-quote (")  
#   \a : ASCII bell (BEL)  
#   \b : ASCII backspace (BS)  
#   \f : ASCII formfeed (FF)  
#   \n : ASCII linefeed (LF)  
#   \N{name} : Character named name in the Unicode database (Unicode only)  
#   \r : Carriage return (CR)  
#   \t : Horizontal tab (TAB)  
#   \uxxxx : Character with 16-bit hex value xxxx  
#   \Uxxxxxxxx : Character with 32-bit hex value xxxxxxxx  
#   \v : ASCII vertical tab (VT)  
#   \000 : Character with octal value 000  
#   \xhh : Character with hex value hh


# Study Drills

test = '''
I'll do a list:
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass
'''
print(test)
