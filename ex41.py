# Learning to Speak Object-Oriented

# class X(Y)：

# class X(object): 
#     def __init__(self, J) 

# class X(object): 
#     def M(self, J) 

# foo = X()
# foo.M(J)
# foo.K = Q

import random
from urllib.request import urlopen
import sys 
# from sys import argv 

WORD_URL = "http://learncodethehardway.org/words.txt" 
WORDS = []
PHRASES = {
	"class %%%(%%%):":
	    "Make a class named %%% that is-a %%%.", 
    "class %%%(object):\n\tdef __init__(self, ***)" :
	    "class %%% has-a __init__ that takes self and *** params.", 
    "class %%%(object):\n\tdef ***(self, @@@)":
	    "class %%% has-a function *** that takes self and @@@ params.", 
    "*** = %%%()":
	    "Set *** to an instance of class %%%.", 
    "***.***(@@@)":
	    "From *** get the *** function, call it with params self, @@@.", 
    "***.*** = '***'":
  	    "From *** get the *** attribute and set it to '***'."
}
print(PHRASES)
print(sys.argv)

if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False 

# 获取 WORD_URL 中的单词并存入 WORDS 中
for word in urlopen(WORD_URL).readlines():
    print(word)   # word 为字节型
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    # 将 WORDS 里面的单词随机排列后,首字母大写后赋给 class_names
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []
   
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        print(param_count)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        print(param_names)
   
    for sentence in snippet, phrase:
        result = sentence[:]  #复制列表：使用列表切片语法[：]可以有效地从第一个元素到最后一个元素进行切片。
        
        for word in class_names:
            result = result.replace("%%%", word, 1)  # 替换类名
            
        for word in other_names:
            result = result.replace("***", word, 1)  # 替换方法名
        
        for word in param_names:
            result = result.replace("@@@", word, 1)  # 替换参数名
        
        results.append(result)
    return results

try:
    # while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets) # 将列表中的所有元素 随机打乱 顺序
        for snippet in snippets:
            phrase = PHRASES[snippet] # 获取对应的值
            question, answer = convert(snippet, phrase) # 替换了对应的类名、方法名、参数名后返回
           
            if PHRASE_FIRST:
                question, answer = answer, question
                print("? ", question)
                user = input("> ")
                while user != answer:  # 由于终端输入受限制，无法成功退出
                    print("Try angin :") 
                    user = input("> ")
                    print(answer)
                # print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
