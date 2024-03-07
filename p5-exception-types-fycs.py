#practical 5- fycs
#Python program to demonstrate different types of exception handling

try:
    # Zero division error
    result = 1 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError: ", e)

try:
    # Name error
    print(non_existent_variable)
except NameError as e:
    print("Caught NameError: ", e)

try:
    # Type error
    "2" + 2
except TypeError as e:
    print("Caught TypeError: ", e)

try:
    # File not found error
    with open("non_existent_file.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print("Caught FileNotFoundError: ", e)

try:
    # Keyboard interrupt
    while True:
        pass
except KeyboardInterrupt as e:
    print("Caught KeyboardInterrupt: ", e)

try:
    # Exception
    raise Exception("This is an exception")
except Exception as e:
    print("Caught Exception: ", e)