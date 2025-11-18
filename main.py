import os
import random
# all_the_cards=os.listdir("flashcards")
# #print(all_the_cards)

all_the_flashcards=os.listdir("flashcards")
all_the_flashcards[random.randint(0, len(all_the_flashcards)-1)]
score=0
used_flashcards=[]

def flashcard_rotator():
    global score
    global used_flashcards
    the_flashcard=all_the_flashcards[random.randint(0, len(all_the_flashcards)-1)]
    while the_flashcard in used_flashcards:
        the_flashcard=all_the_flashcards[random.randint(0, len(all_the_flashcards)-1)]
        if len(used_flashcards)==len(all_the_flashcards):
            print(score)
            break
    f=open("flashcards/"+the_flashcard)
    inside_it=f.read()
    lines=inside_it.split("\n")
    front_start=lines.index(">")
    back_start=lines.index("<")
    front=[*filter(bool, lines[front_start+1: back_start])]
    print(front)
    back=[*filter(bool, lines[back_start+1: ])]
    answer=input(" ")
    if answer.lower().strip()==back[0].lower().strip():
        print("correct ")
        print(back)
        score+=10
    else:
        print("wrong ")
        print(back)
        wait= input("is this correct? Y or N ")
        if wait.upper()=="Y":
            print("correct ")
            print(back)
            score+=10
        else:
            print("wrong ")
            print(back)
            score-=10
    used_flashcards.append(the_flashcard)


    


flashcard_rotator()
  





