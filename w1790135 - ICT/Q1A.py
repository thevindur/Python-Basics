n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

#finding the square values
s1=n1*n1
s2=n2*n2
s3=n3*n3

#finding the cube values
c1=n1*n1*n1
c2=n2*n2*n2
c3=n3*n3*n3

#calculating the required spaces for the given example
x=" "*5
x1=" "*4
y=" "*5
y1=" "*4
z=" "*3

print("\n")
print("Number"+"\t"+"Square"+"\t"+"Cube")
print(n1,x,s1,y,c1)
print(n2,x,s2,y1,c2)
print(n3,x1,s3,z,c3)
