import random
print("Hello, and welcome to the guessing game. I will pick a number between a range you define, and you will get 7 tries to guess the number.\nI will let you know if you are getting too high or too low. Good Luck :)")
name = input("Enter your name: ")
again = 1

def game():
    attempt = 1
    lower = int(input("Please enter the lower bound : "))
    upper = int(input("Please enter the upper bound : "))
    victory = 0
    number = random.randint(lower, upper)
    print("Let's get started!")
    while attempt < 8:
        print("--Attempt " + str(attempt))
        guess = int(input("Guess what number I generated: "))
        if upper < guess or guess < lower:
            print("Oh come on, try again.")
            continue
        else:
            if guess < number:
                print("Too Low.")
                attempt += 1
                continue
            elif guess > number:
                print("Too High")
                attempt += 1
                continue
            else:
                print("Congrats " + name + ", you got it!!")
                victory += 1
                break
    if victory == 0:
        print("The number was " + str(number))


while again == 1:
    game()
    again = int(input("Enter 1 if you would like to play again. "))
    if again == 1:
        print("Here we go :)")

print("Thanks for playing!")

