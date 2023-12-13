import math

while True:
    try:
        x = int(input("Enter the BASE number: "))
        y = int(input("Enter the EXPONENT number: "))
        z = math.pow(x, y)
        print("Result:", z)
    except ValueError:
        print("Please enter valid integer numbers.")
