try:

    x=input("Enter the number:")
    y=int(x)
    sum=0
    lenth=len(x)
    for i in x:
        res=pow(int(i),lenth)
        sum=sum+res
    # print(sum)
    if y==sum:
        print("armstrong")
    else:
        print("not armstrong")
except Exception as e:
    print("Enter the number only")
