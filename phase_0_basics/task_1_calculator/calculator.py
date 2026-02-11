while True:
    user_input_1 = input("Enter your num1: ")
    user_input_2 = input("Enter your num2: ")


    try:
        num1 = float(user_input_1)
        num2 = float(user_input_2)
        sum = num1 + num2
        sub = num1 - num2
        pros = num1 * num2
        div = num1 / num2
        const = num1 ** num2
        print(f"Summury: {sum}, Substraction: {sub}, Event: {pros}, Division: {div}, Constraction: {const}")
        break 
    except ValueError:
        print("Your input is wrong!")
    except ZeroDivisionError:
        print("You can't division by Zero")