try:
    x=int(input("Enter The Number:"))
    if x>0:
        print("Your Number Is Positive")
    else:
        print("Your Number Is negative")
except Exception as e:
    print("Enter the numbers only")
