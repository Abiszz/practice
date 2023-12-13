import math
while True:
    try:

        x=int(input("Enter the number "))
        y=math.factorial(x)
        print(y)
    except Exception as e :
        print("Enter the number only")
