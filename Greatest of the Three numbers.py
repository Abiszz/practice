
while True:
    try:
        x = int(input("Enter The Number one :"))
        y = int(input("Enter The Number two:"))
        z = int(input("Enter The Number three:"))
        if x>y>z :
            print(f"{x} is greatest Number")
        elif y>z>x:
            print(f"{y} is greatest Number")
        else:
            print(f"{z} is greatest Number")

    except Exception as e:
        print("Enter the numbers only")
