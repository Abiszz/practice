while True:
    try:
        x=input("Enter the number:")
        print(x[: :-1])
    except Exception as e:
        print("Enter the number only")
