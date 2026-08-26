#1. Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
"""day_num=int(input("enter a number from 1-7 :"))
match day_num:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
    case _:
        print("invalid input")"""

"""2. Write a program using match case that simulates a simple calculator.

Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case."""
num1=int(input("enter num 1"))
num2=int(input("enter num 2"))
operation=input("choose operation")
match operation:
    case "+":
        sum=num1+num2
        print(sum)
    case "-":
        sub=num1-num2
        print(sub)
    case _:
        print("invalid")

   

    



