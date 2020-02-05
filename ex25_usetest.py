# import ex25  # 引入自定义类
from  ex25 import *  # 在下文中使用ex25中相关方法时，无需在点名ex25.?,可直接对函数进行使用

sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print("words break_words : ", words)

sorted_words = ex25.sort_words(words) 
print("sorted_words :", sorted_words)

ex25.print_first_word(words)
ex25.print_last_word(words)
print("words pop first and last : ", words)

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print("sorted_words pop first and last : ", sorted_words)

sorted_words = ex25.sort_sentence(sentence) 
print("first to words, second to sort :" , sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)


# Study Drills

# 在终端进入python，import ex25 后，help(ex25) 可以查看到关于类的详细情况