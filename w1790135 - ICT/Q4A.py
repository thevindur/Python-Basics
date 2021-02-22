n=9
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
sp=" "*5
print(sp,"Multiplication Table","\n")
print(sp,"","1 2 3 4 5 6 7 8 9 ","\n")
print("-------------------------------")
count=9
a=0
for i in m:
    i = [str(j).rjust(len(str(m[-1][-1]))+1) for j in i]
    while count!=0:
        a=a+1
        count=count-1
        print(a,"|",end="")
        print(''.join(i))
