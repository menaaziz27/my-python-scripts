#Rock paper scissors vs computer 
from random import randint
print("rock ...")
print("paper ...")
print("scissors ...")

player1 = input("Choose your choice : ")
rand_num = randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'

print(f"computer choose {computer}.")

if player1 == computer:
    print("It's a Tie!")
elif player1 == "rock":
    if computer == "paper":
        print("computer wins!")
    elif computer == "scissors":
        print("player1 wins!")
elif player1 == "paper":
    if computer == "rock":
        print("player1 wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player1 == "scissors":
    if computer == "paper":
        print("player1 wins!")
    elif computer == "rock":
        print("computer wins!")
else:
    print("something went wrong")


