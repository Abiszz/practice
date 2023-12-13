import math

strong = 0
x = input("Enter the number:")
z = int(x)
for i in x:
    y = math.factorial(int(i))
    strong += y
if strong == z:
    print(f"{x} is a strong number.")
else:
    print(f"{x} is not a strong number.")
