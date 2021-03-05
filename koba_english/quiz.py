#!/usr/bin/env python3

import csv
import re

def English_quiz():
    words_file = input("Choose a file you want to practice: ")
    with open(words_file) as f:
        reader = csv.reader(f)

        how_many_correct = 0
        how_many_mistake = 0
        for line in reader:
            print("\nMeaning\n" + "##########\n" + line[1] + "\n##########")
            answer = input("Type a word related to the meaning that is displaying : ")
            if answer == line[0]:
                print("Correct!")
                how_many_correct += 1
            else:
                print("Not correct")
                how_many_mistake += 1

        print("Correct number is {}".format(how_many_correct))
        print("Mistake number is {}".format(how_many_mistake))

