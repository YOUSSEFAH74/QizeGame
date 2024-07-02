# ---------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print('-'*50)
        print(key)
        for i in options[question_number - 1]:
            print(i)
        guess = input('Enter (A, B, C or D):').upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1
    display_score(correct_guesses,guesses)
# ---------------------------
def check_answer(answer,guess):
    if answer == guess:
        print('CORRECT!')
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------------
def display_score(correct_guesses,guesses):
    print('-'*50)
    print("RESULTS IS")
    print('-'*50)
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end =" ")
    print()
    print("Guesses: ",end="")
    for i in guesses:
        print(i,end =" ")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score)+" %")
# ---------------------------
def play_again():
    response = input("Do You want to play again?: (Y or N):").upper()
    if response == "Y":
        return True
    else:
        return False   
# ---------------------------
questions = {
    "who created Python?:" : 'A',
    "what year of Python was created?:" : 'B',
    "python is tributed to which comedy group?:":'C',
    "Is the Earth round?:":'A'
}
options = [["A.Guido van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuck"],
           ["A.1989","B.1991","C.2000","D.2016"],
           ["A.Lonely Island","B.Smosh","C.Monty Python","D.SNL"],
           ["A.True","B.False","C.somtimes","D.What's Earth"]]
new_game()
while play_again():
    new_game()
print("THX PRO!!")