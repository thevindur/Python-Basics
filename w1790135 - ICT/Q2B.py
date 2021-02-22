RT=input("Enter the type of room: ")
M=input("Enter the month you wish to make the reservation: ")
D=input("Enter the number of days: ")
N=input("Enter the number of rooms: ")
print("\n")

dr=0
tc=0
tdr=0

try:
    D = int(D)
except ValueError:
    print("Please enter integers for number of days and number of rooms")
    import sys
    sys.exit()
 
try:
    N = int(N)
except ValueError:
    print("Please enter integers for number of days and number of rooms")
    import sys
    sys.exit()

def discount():
    global dr
    global GT
    if M=="Jan" or M=="Feb" or M=="March":
        if D<=2:
            dr=GT*5/100
        elif D<=5:
            dr=GT*10/100
        else:
            dr=GT*15/100

    elif M=="April" or M=="May" or M=="June":
        if D<=2:
            dr=GT*8/100
        elif D<=5:
            dr=GT*13/100
        else:
            dr=GT*18/100

    elif M=="July" or M=="August" or M=="September":
        if D<=2:
            dr=GT*10/100
        elif D<=5:
            dr=GT*15/100
        else:
            dr=GT*20/100

    elif M=="October" or M=="November" or M=="December":
        if D<=2:
            dr=GT*3/100
        elif D<=5:
            dr=GT*8/100
        else:
            dr=GT*11/100


if (N<=5) and (N!=0):
    if (RT=="Double Room") or (RT=="DR"):
        c=12000
        tc=c*N
        GT=tc*D
        discount()
        tdr=dr*N
    elif (RT=="Twin Room") or (RT=="TR"):
        c=17000
        tc=c*N
        GT=tc*D
        discount()
        tdr=dr*N
    elif (RT=="Master Suite") or (RT=="MS"):
        c=24000
        tc=c*N
        GT=tc*D
        discount()
        tdr=dr*N
    else:
        print("There is no such room catagory available.")


NT=GT-dr
print("Total amount :",GT)
print("Discount received :",dr)
print("Total Payable : ",NT)
