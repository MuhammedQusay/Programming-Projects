import random

option = ("rock" , "paper" , "scissors")
p_option = ("1" , "2" , "3")
c_option = ("1" , "2" , "3")


while True:
    computer = random.choice(c_option)
    player = None

    while player not in p_option:
        print("----Rock / Paper / Scissors----")
        player = input("What is your choice?(1 / 2 / 3): ").strip()

    if player == computer:
        print("Its a draw")
    elif (computer == "1" and player == "2") or (computer == "2" and player == "3") or (computer == "3" and player == "1"):
        print("You win")
    else:
        print("You lose")
    
    again = input("Want to play again?(Y / N): ").lower().strip()
    if again != "y":
        break