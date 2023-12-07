
while True:
    try:
        x = int(input("Enter The Number one :"))
        y = int(input("Enter The Number two:"))
        num=0
        if x>y:
            print(f"{x} is greatest Number")
        else:
            print(f"{y} is greatest Number")


    except Exception as e:
        print("Enter the numbers only")
