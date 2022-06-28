# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 23:26:25 2020

@author: Avinash Ranjan
"""

import re

print("Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    equation = ""
    equation = input("Enter Equation:") if previous == 0 else input(str(previous))
    if equation == 'quit':
        print("GoodBye, Human..!")
        run = False

    else:
        equation = re.sub('[a-zA-Z,:()"{}"]', '', equation)

        previous = eval(equation) if previous == 0 else eval(str(equation) + equation)


while run:
    performMath()
