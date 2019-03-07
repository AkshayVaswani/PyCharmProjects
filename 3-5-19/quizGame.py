print("Welcome to the quiz, you will be asked multiple questions of\n\t\t\t varying types, and will be graded based on performance.")
name = input("Enter your name: ").title()
score = 0
print("Lets begin!\nFor the first question, please enter just the letter of the choice of the answer you would like to choose")
first = input("What is 1 + 1?\nA.\t2\nB.\t5\nC.\tsqrt(3)\nD.\tYes\n").upper()
if first == "A":
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please enter just the word that is correct")
second = input("What is the color of the sky?\n").upper()
if "BLUE" in second:
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please enter just the number that is correct")
third = input("What is 21 * 5?\n").upper()
if third == "105":
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please take the answer from the prior answer and divide it by 7")
fourth = input("What is the new value?\n").upper()
if fourth == "15":
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please enter the correct answer based on the answer that you entered to the prior question, not the correct one if it isn't what you entered.")
fifth = input("What is the prior answer +17?\n").upper()
if fifth == str(int(fourth) + 17):
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please take the answer from the prior answer and multiply it by 4")
sixth = input("What is the new value?\n").upper()
if sixth == str(int(fifth) * 4):
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("Lets take a break from the math for a second. For the next question, please tell me what the correct answer's corresponding letter is.")
seventh = input("What is the name if the language we are reading in right now?\nA.\tEnglish\nB.\tSwahili\nC.\tHindi\nD.\tDefinately not\n").upper()
if seventh == "A":
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print("For the next question, please tell me the proper spelling of the word onomatopoeia")
eight = input("Spelling:\n").upper()
if eight == "ONOMATOPOEIA":
    print("Correct!\n")
    score += 1
else:
    print("Not Correct.\n")
print(name+"'s score was "+str(score)+"/8, and your average score is: "+str(float(score/8)*100) + "%.")