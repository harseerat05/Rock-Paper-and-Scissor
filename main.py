import random
computer=random.choice([-1.0,1])

def ask():
    tell=input("Want a rematch?(y/n)")
    decide=tell.lower()
    if decide=="y":
        game()
    else:
        print("Thanks for playing!")




def game():
    
    print('''
        Choices available:\n
        Rock(r)\n
        Paper(p)\n
        Scissors(s)\n
        ''')
    youStr=input("enter your choice :")
    youDict={"r":-1, "p":0, "s":1}
    reverseDict={-1:"Rock", 0:"Paper",1:"Scissors"}
    you=youDict[youStr]
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")
    if(you==computer):
        print("Draw!")
        ask()
    elif((you==-1 and computer==1)or(you==0 and computer==-1)or(you==1 and computer==0)):
        print("You Won!")
        ask()
    elif((computer==-1 and you==1)or(computer==0 and you==-1)or(computer==1 and you==0)):
        print("Computer Won!")
        ask()    
    elif(you!=0 or you!=1 or you!=-1):
       print("Invalid Input")
       ask()
    else:
        print("You Lose!")
        ask()

game()
       

    
