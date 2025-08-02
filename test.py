import random

while True:

    print("\n1.Rock \n 2.Paper \n 3.Scissors")

    guess_game = random.randint(1, 3)
    user_guess = int(input("Guess: "))
    guess = {1: "Rock", 2: "Paper", 3: "Sizer"}
    print()



    print(f"Gamer guess: {guess[user_guess]}")

    print(f"Computer guess: {guess[guess_game]}")

    #1<2
    #1=1
    #3<1
    #3=3
    #2=2
    #2<3
    #

    if user_guess ==guess_game:
        print("No win")
    elif (user_guess==1 and guess_game==3)or\
        (user_guess==2 and guess_game==1)or\
        (user_guess==3 and guess_game==2):
        print("You won")
    else:
        print("You list")
        print()