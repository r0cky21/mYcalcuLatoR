while(True):
    print("\nWelcome to MyCalculatoR")
    print("\n\n select an optoion to perform an operation")
    print("\n 1:Addition")
    print("2:Substration")
    print("3:Multiplication")
    print("4:Division")
    print("5:Exit")

    c = input("enter your choice : ")

    if(c=="1"):
        x=float(input("enter number : "))
        y=float(input("enter number : "))
        print(f"\n\n {x}+{y} = {x+y} " )
        print(f"\n\n ===============")

    elif(c=="2"):
        x=float(input("enter number : "))
        y=float(input("enter number : "))
        print(f"\n\n {x}-{y} = {x-y} " )
        print(f"\n\n ===============")

    elif(c=="3"):
        x=float(input("enter number : "))
        y=float(input("enter number : "))
        print(f"\n\n {x}*{y} = {x*y} " )
        print(f"\n\n ===============")

    elif(c=="4"):
        x=float(input("enter number : "))
        y=float(input("enter number : "))
        print(f"\n\n {x}/{y} = {x/y} " )
        print(f"\n\n ===============")

    elif(c=="5"):
        con=input("do you want to exit (Y/N) : ")
        if ( con.lower() == "y" ):
            break
        elif (con.lower() == "n"):
            continue

        else:
            print( "press <enter> to close")
        

input(" press<enter> to exit")
        
        
