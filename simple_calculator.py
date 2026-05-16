


while True:

        user_input = input("If you want to start the job, type 'go';" \
            "if you want to stop job, type 'exit': ")
        if user_input == "go":

            numb1 = int(input("Enter the first integer: "))
            numb2 = int(input("Enter the second integer: "))

            action = input("Enter the action to perform: ")
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

        elif user_input == "exit":
            break

        else:
            print("I didn't quite understand what you meant.")

