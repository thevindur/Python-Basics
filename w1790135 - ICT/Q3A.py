x=input("Do you really want to run this program? (y/n) : ")
x=x.upper()

if x=="Y" or x=="N" or x=="Q":
    while x=="Y" or x=="N" or x=="Q":
        if x=="Q":
            print("Exiting the Program")
            import sys
            sys.exit()
        elif x=="N":
            print("You decided to leave. See you again!” ")
            break
        #elif x=="Y":
        #You can run the program.Enter the code required to run the program
else:
    print("Invalid selection is entered")    
