# def circle_area(radius) :
#     phi= 3.14
#     result= phi * radius**2
#     text= f"Area of the circle is {result}"
#     return text

# print(circle_area(2))

from random import randint

title = "Rock Paper-scissor Game"
print(title)
print(f"{'=' * len(title)}")

weapon = ["rock", "paper", "scissor"]

player = input("Which is your weapon? (rock/paper/scissor)\n")
computer = weapon[randint(0, 2)]

if player == 'rock':
    if computer == 'rock':
        print("player uses", player)
        print("computer uses", computer)
        print("Nobody wins!")
    elif computer == 'paper':
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == 'scissor':
        print("player uses", player)
        print("computer uses", computer)
        print("player wins!")

if player == 'paper':
    if computer == 'paper':
        print("player uses", player)
        print("computer uses", computer)
        print("Nobody wins!")
    elif computer == 'rock':
        print("player uses", player)
        print("computer uses", computer)
        print("player wins!")
    elif computer == 'scissor':
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")

if player == 'scissor':
    if computer == 'scissor':
        print("player uses", player)
        print("computer uses", computer)
        print("Nobody wins!")
    elif computer == 'rock':
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == 'paper':
        print("player uses", player)
        print("computer uses", computer)
        print("player wins!")

else:
    print('Your input a wrong weapon')
