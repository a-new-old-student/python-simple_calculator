numb1 = int(input("Enter the first integer: "))
numb2 = int(input("Enter the second integer: "))

action = input("Enter the action to perfom: ")

if action == "plus":
    print(numb1 + numb2)
elif action == "subtract":
    print(numb1 - numb2)
elif action == "multiply":
    print(numb1 * numb2)
elif action == "degree":
    print(numb1 ** numb2) 
elif action == "divide":
    if numb2 == 0:
        print("Cannot divide by zero")
    else:
        print(numb1 / numb2)
else:
    print("Invalid action")