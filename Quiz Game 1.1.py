#--------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answers(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
#--------------------------
def check_answers(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
#--------------------------
def display_score(correct_guesses, guesses):
    print("------------------")
    print("RESULTS")
    print("------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your Score is: "+str(score)+"%")
#--------------------------
def play_again():

    response = input("Do you want to play again?: (yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
#--------------------------

questions = { #Diccionario
    "Who created Python?: ": "A",
    "What year was Python created?:": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the earth round: ": "A"
}

options = [["A. Guido van Rossum", "B. Elen Musk", "C. Bill Gates","D. Mark Zuckerberg"],
           ["A. 1986","B. 1991","C. 2000","D. 2016"],
           ["A. Lonely Island","B. Smoch","C. Monty Python","D. SNL"],
           ["A. True,","B. False","C. Sometimes","D. IDK"]]

new_game()

while play_again():
    new_game()

print("See you next time!")