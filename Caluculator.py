import re

print("My Calculator")
print("Quit to exit")

execute_program = True
previous_execution = 0


def perform_calculations():
    global execute_program
    global previous_execution
    equation = ""
    if previous_execution == 0:
        equation = input("Enter equation")
    else:
        equation = input(str(previous_execution))
    if equation == "quit":
        print("Thank You")
        execute_program = False
    else:
        re.sub('[a-zA-Z()",:]', "", equation)
        if previous_execution == 0:
            previous_execution = eval(equation)
        else:
            previous_execution = eval(str(previous_execution) + str(equation))


while execute_program:
    perform_calculations()
