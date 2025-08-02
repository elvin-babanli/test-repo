import random

while True:
    game_choose = random.randint(1, 3)
    option = int(input("Select 1.Rock, 2.Paper, 3.Scissors: "))

    rock = 1
    paper = 2
    scissors = 3
    if game_choose == rock and option == paper:
        print("Computer choose: ",game_choose)
        print("You win!")
    elif game_choose == rock and option == scissors:
        print("Computer choose: ",game_choose)
        print("Computer wins!")
    elif game_choose == rock and option == rock:
        print("Computer choose: ",game_choose)
        print("No win!")
    elif game_choose == paper and option == rock:
        print("Computer choose: ",game_choose)
        print("Computer wins!")
    elif game_choose == paper and option == paper:
        print("Computer choose: ",game_choose)
        print("No win!")
    elif game_choose == paper and option == scissors:
        print("Computer choose: ",game_choose)
        print("You win!")
    elif game_choose == scissors and option == rock:
        print("Computer choose: ",game_choose)
        print("You win!")
    elif game_choose == scissors and option == paper:
        print("Computer choose: ",game_choose)
        print("Computer wins!")
    elif game_choose == scissors and option == scissors:
        print("Computer choose: ",game_choose)
        print("No win!")



