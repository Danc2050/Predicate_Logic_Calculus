from files import*
import os
def Logic():
    print("(1) - Quantifiers and Variables\n(2) - Predicates and Names\n(3) - Formation Rules\n(4) - Refutation Trees\n(5) - Identity\n(6) - Quiz\n(7) - Main Menu\n")
    x = int(input())
    if x == 6: Quiz("Quiz")
    else: open_file("", x)
def Calculus():
    print("(0) - Intro to Predicate Calculus\n(1) - Rules for Universal Quantifier\n(2) - Rules for Existential Quantifier\n(3) - Identity Predicate\n(4) - Theorems and Quantifier Exchange\n(5) - Main Menu\n")
    x = int(input())
    open_filePC("", x)

def OpenFile(rel_path):
    location = find_file(rel_path)
    f = open(location, 'r')
    for line in f: print(line)

# http://www.cse.msu.edu/~pramanik/teaching/courses/cse260/11s/lectures/Tubai/Feb-6/predicate
def Quiz(rel_path):
    location = find_file(rel_path)
    f = open(location, 'r')
    quizR = [None] * 12
    for line in f:
        print(line)
    print("\nPlease enter your answers to the above questions (Using T or F or a letter where applicable).")
    key = [" ", "T", "F", "F", "T", "T", "T", "a", "T", "F", "F", "T", "F"]
    for x in range (1, 12):
        quizR[x] = input()
    for x in range (1, 12):
        if(quizR[x] == key[x]):
            print("Answer " + quizR[x] + " is correct")
        else:
            print("Answer " + quizR[x] + " is incorrect")
    return quizR

def Main():
    OpenFile("Introduction.rtf")
    x = 0
    while x != 3:
        print("(1) - Predicate Logic\n(2) - Predicate Calculus\n(3) - Exit")
        x = int(input())
        a = os.system("clear") #Enable if you want the screen cleared before every new tutorial section selected
        if (x == 1): Logic()
        if(x == 2): Calculus()
        if(x == 3): exit(1)