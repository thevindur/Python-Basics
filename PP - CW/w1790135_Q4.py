# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 2019595
# Date: 15.04.2020


a=0     #progress_counter
b=0     #trailing_counter
c=0     #retriever_counter
d=0     #exclude_counter
t=0     #total_counter
s="*"   #star

def horizontalhistogram():
    print("\n")
    print("Progress",a,"\t",":",a*s)
    print("Trailing",b,"\t",":",b*s)
    print("Retriever",c,"\t",":",c*s)
    print("Exclude",d,"\t",":",d*s)
    print("\n")
    print(t,"Outcomes in Total")
    
def verticalhistogram():
    global a
    global b
    global c
    global d
    sp = " "
    print("\n")
    print("Progress","Trailing","Retriever","Exclude")
    while (a>=1 or b>=1 or c>=1 or d>=1):
        if a>0:
            p="*"
        else:
            p=" "

        if b>0:
            q="*"
        else:
            q=" "

        if c>0:
            r="*"
        else:
            r=" "

        if d>0:
            s="*"
        else:
            s=" "

        print(sp*3+p + "\t" + sp*4+q + "\t" + sp*6+r + "\t" + sp*7+s)
        a=a-1
        b=b-1
        c=c-1
        d=d-1
    print("\n")
    print(t,"Outcomes in Total")


for x in range(0,10):
    
    passCredits=[120,100,100,80,60,40,20,20,20,0]
    deferCredits=[0,20,0,20,40,40,40,20,0,0]
    failCredits=[0,0,20,20,20,40,60,80,100,120]
    
    passDefer = passCredits[x] + deferCredits[x]
    t=t+1
    if passCredits[x] == 120:
        print("Progress")
        a=a+1
    elif passCredits[x] >= 100:
        print("Progress - Module Trailer")
        b=b+1
    elif passDefer >= 60:
        print("Do not Progress - Module Retriever")
        c=c+1
    else:
        print("Exclude")
        d=d+1

horizontalhistogram()
verticalhistogram()
    
