#coding=utf-8

# Numbers and Math

#   +: plus
#   -: minus
#   /: slash
#   *: asterisk
#   %: percent
#   <: less-than
#   >: greater-than
#   <=: less-than-equal
#   >=: greater-than-equal

# 我要开始数我的小鸡了
print("I will now count my chickens:") 
# 母鸡有30只
print("Hens", 25 + 30 / 6)
# 公鸡有97只
print("Roosters", 100 - 25 * 3 % 4)
# 我要开始数鸡蛋了：
print("Now I will count the eggs:")
# 鸡蛋有7个
print("Eggs",3+2+1-5+4%2-1/4+6) 
print("Is it true that 3+2<5-7?") 
print("Is it true that 3+2<5-7?",3+2<5-7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
# 哦，这就是为什么它是假的。
print("Oh, that's why it's False.")
# 再来点
print("How about some more.") 
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Study Drills
print(float(3+2+1-5+4%3-1/4+6))
print(float(10/3))

# 十六进制整数41
print(float(0x41))   
# 八进制整数41    
print(float(0o41))     
# 二进制整数1101    
print(float(0b1101))  
# 保留20位小数
print('%.20f' % (4/3))
# 保留4位小数
from decimal import Decimal as dc 
print(dc('5.026').quantize(dc('0.0000')))