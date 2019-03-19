import random
name = input("Please Enter Your Name: ") # Name input
print("We are going to be playing rock paper scissors lizard spock.\n\t You will enter a move, and the computer will generate \n\ta move, and then the winner will be decided. You can play \n\tas long is you would like. Good Luck.")
gameGo = True
score = 0


def move(x): # Translates a number to its respective String
    if x == 0:
        return "ROCK"
    elif x == 1:
        return "PAPER"
    elif x == 2:
        return "SCISSORS"
    elif x == 3:
        return "LIZARD"
    else:
        return "SPOCK"


def game():
    global score # Keep track of the score
    player = input("Please type out one of the following, if you make a typo the game will run again. \n\tRock\n\tPaper\n\tScissors\n\tLizard\n\tSpock\n\t").upper()
    computer = random.randint(0, 4) # Generates a random number
    compMove = move(computer) # Inputs the random number to move(x) to receive the string

    print("The computer threw " + compMove.title() + ".")
    if compMove.upper() == player.upper(): # A bunch of if statements to compare the player's move with the computer to determine winner.
        return "ITS A TIE!"
    elif player.upper() == "ROCK":
        if compMove.upper() == "LIZARD" or compMove.upper() == "SCISSORS":
            score += 1
            return "YOU WIN"
        elif compMove.upper() == "PAPER" or compMove.upper() == "SPOCK":
            return "YOU LOSE"
    elif player.upper() == "PAPER":
        if compMove.upper() == "ROCK" or compMove.upper() == "SPOCK":
            score += 1
            return "YOU WIN"
        elif compMove.upper() == "SCISSORS" or compMove.upper() == "LIZARD":
            return "YOU LOSE"
    elif player.upper() == "SCISSORS":
        if compMove.upper() == "PAPER" or compMove.upper() == "LIZARD":
            score += 1
            return "YOU WIN"
        elif compMove.upper() == "ROCK" or compMove.upper() == "SPOCK":
            return "YOU LOSE"
    elif player.upper() == "LIZARD":
        if compMove.upper() == "SPOCK" or compMove.upper() == "PAPER":
            score += 1
            return "YOU WIN"
        elif compMove.upper() == "ROCK" or compMove.upper() == "SCISSORS":
            return "YOU LOSE"
    elif player.upper() == "SPOCK":
        if compMove.upper() == "ROCK" or compMove.upper() == "SCISSORS":
            score += 1
            return "YOU WIN"
        elif compMove.upper() == "PAPER" or compMove.upper() == "LIZARD":
            return "YOU LOSE"
    else:
        print("T Y P O")
        game()


while gameGo: # Runs the game again upon user choice
    print(game())
    temp = input(name+"'s score is: "+str(score)+". Go again? Y/N \t").upper() # Asks the user if they want to play again
    if temp == "Y":
        gameGo = True
    else:
        gameGo = False

print("Thanks for playing :)") # :)
