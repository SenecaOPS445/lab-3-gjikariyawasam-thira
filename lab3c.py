#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''

#Author ID: Jihan Kariyawasam

def operate(number1, number2, operator):
    if operator == 'add':
        total = number1 + number2
    elif operator == 'subtract':
        total = number1 - number2
    elif operator == 'multiply':
        total = number1 * number2
    else: 
        total = 'Error: function operator can be "add", "subtract", or "multiply"'
    return total

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
