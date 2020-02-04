# Prompting and Passing

from sys import argv 
script, user_name = argv

prompt = '>>> '  # 进行输入提示

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
   Alright, so you said {likes} about liking me.
   You live in {lives}.  Not sure where that is.
   And you have a {computer} computer.  Nice.
""")

# Study Drills

print("""
ZORK(http://textadventures.co.uk/games/play/5zyoqrsugeopel3ffhz_vq)

Welcome to ZORK.
Release 13 / Serial number 040826 / Inform v6.14 Library 6/7
West of House
This is an open field west of a white house, with a boarded front door.
There is a small mailbox here.
A rubber mat saying 'Welcome to Zork!' lies by the door.
""")
word = input(prompt)
if str(word).__contains__("west") :
    print("""
    There is a small mailbox here.
    A rubber mat saying 'Welcome to Zork!' lies by the door.
    """)
elif str(word).__contains__("east") :
    print("""
    The door is locked, and there is evidently no key.
    """)
elif str(word).__contains__("north") :
    print("""
    The windows are all barred.
    """)
elif str(word).__contains__("south"):
    print("""
    South of House
    You are facing the south side of a white house.  There is no door here, and all the windows are barred.
    """)