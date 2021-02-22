# Name: Thevindu Rajapakse
# Date: 12th Feb 2020
# Description: Tutorial 2

# Question 3 a
item1 = int(input("Enter a value : "))
item2 = int(input("Enter a value : "))
item3 = item1+item2
print(item3,"\n")

# Question 3 b
meal_cost = int(input("Enter the meal value : £"))
tip = meal_cost*0.1
total = meal_cost + tip
print("Total Meal cost is £"+str(total),"Meal Cost £"+str(meal_cost),"Tip is £"+str(tip),sep="\n")
print("\n")

# Question 4
num = 5
print(num)
num = num + 2
print(num)
num = num // 3 * 6
print(num)
print(7 + 15 % 4)
num = 24 // 3 // 4
print(num,"\n")

# Question 5 a
a = "Hello out there."
print(a)
b = 'Hello again.'
print(b,"\n")

# Question 5 c
a = '10'
b = '99'
c = a + b
print (c)
c = int(c)
print (c,"\n")

# Question 5 d
a = '10'
b = '9'
c = a + b
print (c)
c = int(c)
print (c,"\n")

# Question 6 a
name = input('Please enter your name: \n')
print('Hello', name,"\n")

# Question 6 b
name = input('Please enter your name: \n')
print('Hello', name)
age = int(input("Please enter your age : \n"))
print("your age is "+str(age),"\n")

# Question 7
print("test\\test2\\answers.txt","\n")

# Question 8
the_text = input('Enter some text.\n')
#print - version 1
print('This is what you entered: ')
print(the_text)
#print - version 2
print('This is what you entered:', the_text)
#print - version 3
print('This is what you entered:', end=' ')
print(the_text,"\n")

# Quetion 9
print("A", end = ' ')
print("B", end = ' ')
print("C", end = ' ')
print("D", end = '\n')
print("\n")

# Question 10

# Lecture 2 Question 1
pets=int(input("Enter No of Pets : "))
print("You have "+str(pets)+" pets","\n")

# Lecture 2 Question 2
run_total=0
count=5
while(count>1):
    add=int(input("Enter the Value : "))
    run_total = run_total + add
    print(run_total)
    count=count-1
print("\n")

# Lecture 2 Question 3
total=0
num_1=int(input("Enter No 1 : "))
num_2=int(input("Enter No 2 : "))
total=num_1+num_2
print(total,"\n")

# Lecture 2 Question 4
cost_of_item = int(input("Enter the Cost of Item : "))
cash_paid = int(input("Enter the Cash Paid : "))
change = cash_paid - cost_of_item
print(change,"\n")

# Lecture 2 Question 5
num_1=int(input("Enter No 1 : "))
num_2=int(input("Enter No 2 : "))
num_3=int(input("Enter No 3 : "))
avg = (num_1+num_2+num_3)/3
print(avg,"\n")

# Question 11
c=int(input("Enter the Temperature in celtigrades : "))
f=(9/5)**c+32
print("The Temperature is "+str(f)," Farenheit","\n")

# Question 12
length = int(input("Enter the Length : "))
width = int(input("Enter the Width : "))
height = int(input("Enter the Height : "))
volume = length*width*height
print("The Volume of the Box is",volume,"\n")

# Question 13
meters=int(input("Enter value in meters : "))
cm=meters*100
print("The Value you entered is",str(cm)+" centimeters","\n")

# Question 14
n = input("Please enter an integer: ")
try:
 n = int(n)
except ValueError:
 print("Requires a valid integer!")
print("\n")

# Question 15
try:
    x=2/0
except ZeroDivisionError:
    print("Cannot divide by zero")
