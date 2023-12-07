try:
    x = int(input("Enter The Number:"))
    num=0
    for i in range(x+1):
        num=num+i
    print(num)


except Exception as e:
    print("Enter the numbers only")
