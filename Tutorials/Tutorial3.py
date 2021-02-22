def question1a():
    #Question 1(a)
    n = int(input('Give me a number over 100:'))
    if n <= 100:
     print(n, 'is not over 100')
    else:
        print(n, 'is over 100')

def question1b():
    #Question 1(b)
    x= int(input("Please enter your age : "))
    #try:
        #x=int(x)
    #except Exception:
       # print("Please enter a valid input")
    if x>18:
        print("Can Vote")
    else:
        print("Cannot Vote")

def question2a():
    #Question 2(a)
    x = int(input('Give me a number: '))
    if x < 0:
     print(x, 'is negative')
    else:
     print(x, 'is positive')

def question2b():
    #Question 2(b)
    marks=int(input("Enter Your Marks : "))
    if marks>=40:
        print("PASS")
    else:
        print("FAIL")

def question2c():
    #Question 2(c)
    n=int(input("Enter the Temperature in Centigrade : "))
    if n>19:
        print("HOT")
    else:
        print("COLD")

def question2d():
    x = int(input('Give me a number: '))
    n=x%2
    if (n==1):
        print("Odd Number")
    else:
        print("Even Number")

def question3():
    import random
    x=random.randint(1,2)
    if x==1:
        print("Heads")
    else:
        print("Tails")

def question4a():
    n=int(input("Enter '1' if you want to convert from Celsius to Fahrenheit or Enter ‘2’ if you want to convert from Fahrenheit to Celsius: "))
    if n==1:
        c=int(input("Enter the Temperature in Celsius : "))
        f=(9/5)**c+32
        print("The Temperature is "+str(f)," Farenheit")
    elif n==2:
        f=int(input("Enter the Temperature in Farenheit : "))
        c = (f-32) * 5 / 9
        print("The Temperature is "+str(c)," Celsius")
    else:
        print("Invalid option Entered")
    
def question4b():
    n1=int(input("Enter integer 1 : "))
    n2=int(input("Enter integer 2 : "))
    x=input("Enter the operater you require(+,-,*,/) : ")
    if x=="+":
        tot=n1+n2
        print("Your answer is",tot)
    elif x=="-":
        tot=n1-n2
        print("Your answer is",tot)
    elif x=="*":
        tot=n1*n2
        print("Your answer is",tot)
    elif x=="/":
        try:
          tot=n1/n2
          print("Your answer is",tot)
        except Exception:
            print("Error")
    else:
        print("Not a valid operator")
    


def question4c():
    cost=int(input("Enter the cost of the meal : "))
    satisfy=int(input("Rate Please : 1 = Totally satisfied, 2 = Satisfied, 3 =Dissatisfied : "))
    tip=0
    if satisfy==1:
        tip=cost*0.2
    elif satisfy==2:
        tip=cost*0.15
    elif satisfy==3:
        tip=cost*0.1
    else:
        print("Invalid Input")
    print("Your Satisfaction Level is",satisfy)
    print("Your Tip is",tip)

def question5b():
    m = int(input('Give me number between 1 and 10:'))
    if m >= 1 and m < 11:
     print('Well done! You gave me:',m)

def question5d():
    mark=int(input("Enter your mark: "))
    if mark<0 or mark>100:
     print("Invalid mark")
    elif mark >= 70:
     print("Exceptional result!")
    elif mark >= 40:
     print("Satisfactory result!")
    else:
     print("You have failed.")

def question5f():
    x = 10
    if not x > 10:
     print("not returned True")
    else:
     print("not returned False")

def question6():
    n=input("Do you like Python : ")
    n=n.upper()
    if (n=="YES") or (n=="Y"):
        print("you are on the right course")
    elif (n=="NO") or (n=="N"):
        print("you might change your mind)")
    else:
        print("I did not understand")


print("The Following are the questions in the program. Please Enter the question number only(e.g. 1a) or enter letter 'q' to terminate the program")
print(" "+
      "1a - Determine if a number is less than 100 ","\n",
      "1b - Determine if you can Vote","\n",
      "2a - Determine if a number is Positive or Negative","\n",
      "2b - Determine if you have Pass or Failed","\n",
      "2c - Determine if its Cold or Hot","\n",
      "2d - Determine if a number is Odd or Even","\n",
      "3  - Flip a coin","\n",
      "4a - Farenheit to Celcius or Celcius to Farenheit","\n",
      "4b - Calculator","\n",
      "4c - Calculating the Tip","\n",
      "5b - Printing a number between 1 and 10","\n",
      "5d - Determinig your Grade based on the mark","\n",
      "5f - Understanding the not operator","\n",
      "6  - Do you like Python","\n",)


answer=input("Please enter the Question number:")
while answer!="q":
    if answer=="1a":
        question1a()
    elif answer=="1b":
        question1b()
    elif answer=="2a":
        question2a()
    elif answer=="2b":
        question2b()
    elif answer=="2c":
        question2c()
    elif answer=="2d":
        question2d()
    elif answer=="3":
        question3()
    elif answer=="4a":
        question4a()
    elif answer=="4b":
        question4b()
    elif answer=="4c":
        question4c()
    elif answer=="5b":
        question5b()
    elif answer=="5d":
        question5d()
    elif answer=="5f":
        question5f()
    elif answer=="6":
        question6()
    else:
        print("There is no such Question")
    answer=input("Please enter the Question number:")
