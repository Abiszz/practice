while True:
    try:
        x = input("Enter The Year")
        if len(x) ==4:
            y = len(x)
            z = x[-1]
            a = x[-2]

            if int(z) == 0 and int(a) == 0:
                if int(x[:2]) % 4==0:
                    print("leap year")
                else:
                    print("not leap year")
            elif int(z) != 0 or int(a) != 0:
                if int(x[2:]) % 4==0:
                    print("leap year")
                else:
                    print("not leap year")
        else:
            print("Enter year only")



    except Exception as e:
        print("Enter year only")

