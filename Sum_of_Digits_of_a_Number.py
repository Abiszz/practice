while True:
    try:
        x=input("Enter the number:")
        sum=0
        for i in x:
            sum=sum+int(i)
        print(sum)
    except Exception as e:
        print("Enter the number only")
