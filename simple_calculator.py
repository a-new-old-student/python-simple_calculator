numb1 = int(input("Enter the first integer: "))
numb2 = int(input("Enter the second integer: "))

action = input("Enter the action to perfom: ")

if action == "plus" or action == "+":
    print("Result: ", numb1 + numb2)
elif action == "subtract" or action == "-":
    print("Result: ", numb1 - numb2)
elif action == "multiply" or action == "*":
    print("Result: ", numb1 * numb2)
elif action == "degree" or action == "**":
    print("Result: ", numb1 ** numb2) 
elif action == "divide" or action == "/":
    if numb2 == 0:
        print("Cannot divide by zero")
    else:
        print("Result: ", numb1 / numb2)
else:
    print("Invalid action")