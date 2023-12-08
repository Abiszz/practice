try:
    x = int(input("Enter The Number:"))
    if x % 2 == 0:
        print("Your Number Is even")
    else:
        print("Your Number Is odd")
except Exception as e:
    print("Enter the numbers only")
