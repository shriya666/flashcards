import os
all_the_cards=os.listdir("flashcards")
print(all_the_cards)

f=open("flashcards/example_a")
inside_it=f.read()
lines=inside_it.split("\n")
front_start=lines.index(">")
back_start=lines.index("<")
front=[*filter(bool, lines[front_start+1: back_start])]
print(front)
back=[*filter(bool, lines[back_start+1: ])]
answer=input(" ")
if answer==back[0]:
    print("correct ")
    print(back)
else:
    print(back)


