from operations import addition
from operations import division
from operations import multiplication
from operations import subtraction

print(
        "\nWelcome to the calculator program."
        "\nSelect the following options. ".upper()
        )

print("\na. Addition "
      "\nb. Subtraction "
      "\nc. Multiplication "
      "\nd. Division "
      "\n"
      "\nWrite (quit) to exit the program."
      )

while True:
    try:
        operation = input("\nChoose the operation: ")
        if operation.lower() == "quit":
            break

        n1 = float(input("First Number: "))
        n2 = float(input("Second Number: "))

        if operation == "a":
            print(addition(n1, n2))
        elif operation == "b":
            print(subtraction(n1, n2))
        elif operation == "c":
            print(multiplication(n1, n2))
        elif operation == "d":
            print(division(n1, n2))
        else:
            print("Error! Choose a correct operation.")

    except ValueError:
        print("Error! Just use digits.")
