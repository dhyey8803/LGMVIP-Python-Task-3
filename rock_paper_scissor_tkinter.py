# Rock, Paper & Scissor Game:

from tkinter import *
import random

score=5
player_score=0
round=0
comp_score=0

def game():
    global score
    global player_score
    global comp_score
    global round

    if round >= score:
        return

    list1=["rock","paper","scissor"]
    comp=random.choice(list1)
    player=player_choice.get().lower()

    if player[0]==comp[0]:
        result="Tie!"

    elif (player[0]=="r" and comp=="scissor")or(player[0]=="p" and comp=="rock")or(player[0]=="s" and comp=="paper"):
        player_score+=1
        result="Player score 1 point!"

    elif (player[0]=="r" and comp=="paper")or(player[0]=="p" and comp=="scissor")or(player[0]=="s" and comp=="rock"):
        comp_score += 1
        result = "Computer score 1 point!"

    else:
        result="Invalid Choice!"

    round+=1
    update_score()
    result1.config(text=f"Player: {player} \n Computer: {comp} \n Result: {result}")
    if round == score:
        winner()
    player_choice.set("")

def update_score():
    player_score_label.config(text=f'Player Score: {player_score}')
    comp_score_label.config(text=f'Computer Score: {comp_score}')

def winner():
    global score
    global player_score
    global comp_score
    print("\n")
    if player_score>comp_score:
        result1.config(text=f"Player won the game by {player_score}:{comp_score}")
    elif comp_score>player_score:
        result1.config(text=f"Computer won the game by {comp_score}:{player_score}")
    else:
        result1.config(text=f"Game Tie by {player_score}:{comp_score}")

def reset():
    global score
    global player_score
    global comp_score
    player_score=0
    comp_score=0
    player_choice.set("")
    update_score()
    result1.config(text="")

window=Tk()
window.title("Game")
window.geometry("600x600")
window.config(background="light pink")

label=Label(window,text="Rock, Paper & Scissor Game",font=("algerian",20,"bold"),bg="light pink",fg="black")
label.pack(pady=5)
label4=Label(window,text="RULES:-\n 1. It's a 5 pointer game!\n 2. R(Rock), P(Paper), S(Scissor)",font=("arial",15,"normal"),bg="light pink",fg="black")
label4.pack(pady=10)

label2=Label(window,text='Player',font=("algerian",20,"bold"),bg="light pink",fg="black")
label2.pack(pady=5)
player_choice=StringVar()
entry2=Entry(window,textvariable=player_choice,font=("algerian",20,"bold"),bg="white",fg="black")
entry2.pack(pady=10)

submit=Button(window,text='Submit',font=("algerian",16,"bold"),bg="black",fg="pink",command=game)
submit.pack(pady=10)

player_score_label = Label(window, text=f"Player Score: {player_score}", font=("algerian", 20, "bold"), bg="light pink", fg="black")
player_score_label.pack(pady=10)
comp_score_label= Label(window, text=f"Computer Score: {comp_score}", font=("algerian", 20, "bold"), bg="light pink", fg="black")
comp_score_label.pack(pady=10)

result1=Label(window,text='',font=("algerian",16,"normal"), bg="white", fg="black")
result1.pack(padx=60,pady=10)

reset=Button(window,text='Restart',font=("algerian",16,"bold"),bg="black",fg="pink",command=reset)
reset.pack(pady=10)

window.mainloop()