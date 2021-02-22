print("Please select 1 to convert yards to miles and 2 to convert miles to yards.")
x=int(input("Enter the conversion choice: "))

miles=0
yards=0
if (x==1) or (x==2):
    if (x==1):
        yards=input("Enter the distance in yards: ")
        try:
            yards = int(yards)
            miles = yards/1760
            print("Equivalent distance in miles:",miles)
        except ValueError:
            print("Please restart the program and enter numbers only as input. ")
        
        
    else:
        miles=int(input("Enter the distance in miles: "))
        try:
            miles = int(miles)
            yards = miles*1760
            print("Equivalent distance in yards:",yards)
        except ValueError:
            print("Please restart the program and enter numbers only as input. ")

else:
    print("Invalid input")
