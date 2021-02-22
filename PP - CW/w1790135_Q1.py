# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2019595
# Date: 29.03.2020


def credit():
    if totalCredits != 120:
        print("Total Incorrect! Please make sure that Total Credits is 120")
    else:
        passDefer = passCredits + deferCredits
        if passCredits == 120:
            print("Progress")
        elif passCredits >= 100:
            print("Progress - Module Trailer")
        elif passDefer >= 60:
            print("Do not Progress - Module Retriever")
        else:
            print("Exclude")


passCredits=(input("Enter the Number of Pass Credits : ") or "0" )
deferCredits=(input("Enter the Number of Defer Credits : ") or "0" )
failCredits=(input("Enter the Number of Fail Credits : ") or "0" )

try:
    passCredits=int(passCredits)
    deferCredits=int(deferCredits)
    failCredits=int(failCredits)

#Range Validity
    
    if (passCredits in range(0,121,20)) and (deferCredits in range(0,121,20)) and (failCredits in range(0,121,20)):
        totalCredits = passCredits + deferCredits + failCredits

        credit()
    else:
        print("Range Error!")


#Integer Validity
        
except ValueError:
    print("Integer Required. Please Enter An Integer!")
