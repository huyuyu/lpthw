# import ex40_mystuff as stuff

# stuff.apple()
# print(stuff.tangerine)
# print(stuff.mystuff['apple'])

class MyStuff(object): 
    def __init__(self): # 初始化
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
print(thing.tangerine)
thing.apple()



# dict style 
#   mystuff['apples']
# module style
#   mystuff.apples()    
#   print(mystuff.tangerine) 
# class style
#   thing = MyStuff()  同module相比，多一个实例化的操作
#   thing.apples()
#   print(thing.tangerine)


class Song(object):
   
    def __init__(self, lyrics):
        self.lyrics = lyrics  # 属性 ，不是 变量
        self.sing_me_a_song_str = [ 
                    "String Song",
                    "Happy birthday to you", 
                    "I don't want to get sued",
                    "So I'll stop right there"]
    
    def sing_me_a_song(self): 
        for line in self.lyrics:
            print(line)

happy_bday = Song([ "Happy birthday to you", 
                    "I don't want to get sued",
                    "So I'll stop right there"]) 

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song() 
bulls_on_parade.sing_me_a_song()

# Study Drills

print("String Song : {}".format(happy_bday.sing_me_a_song_str))
