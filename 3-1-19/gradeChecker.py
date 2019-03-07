number = int(input("How many grades would you like to enter?"))
checker = str(input("Would you like an average calculated? Y/N ")).upper()
sum = 0
for i in range(number):
    grade = int(input("What is your numeric grade? "))
    if grade >= 90:
        print("You earned an A!")
    elif 80 <= grade <= 89:
        print("You earned a B!")
    elif 70 <= grade <= 79:
        print("You earned a C!")
    elif 60 <= grade <= 69:
        print("You earned a D!")
    else:
        print("You earned a F!")
    sum += grade

if checker == "Y":
    print("Your average grade is " + str(sum / number))

