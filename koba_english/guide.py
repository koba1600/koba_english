#!/usr/bin/env python3

from quiz import *

def Introduction():
    print("Welcome to KobaEnglish")
    answer = input("If you want to contine, press 'Enter'! (if press 'q', this program is shutting down)")

    if answer == "q":
        print("Bye!")
    else:
        English_quiz()
    
