import re

print("Our magical calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performmath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation : ")
    else:
        equation = input(str(previous))

        
    if equation == 'quit':
        print("Good bye , have a nice day :)")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        
        
while run:
    performmath()
