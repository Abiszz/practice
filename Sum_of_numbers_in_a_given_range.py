
while True:
    try:
        x = int(input("Enter The Number one :"))
        y = int(input("Enter The Number two:"))
        num=0
        for i in range(x,y+1):
            num=num+i
            print(num)


    except Exception as e:
        print("Enter the numbers only")
