x=int(input("Enter the Value of X in Cartesian System : "))
y=int(input("Enter the Value of Y in Cartesian System : "))
if (x==0)and(y==0):
    print("This belong to Quadrant-I(+,+), Quadrant-II(-,+), Quadrant-III(-,-) and Quadrant-IV(+,-)")
elif (x>0)and(y>0):
    print("This belong to Quadrant-I(+,+)")
elif (x<0)and(y>0):
    print("This belong to Quadrant-II(-,+)")
elif (x<0)and(y<0):
    print("This belong to Quadrant-III(-,-)")
elif (x>0)and(y<0):
    print("This belong to Quadrant-IV(+,-)")
else:
    print("Please check your Input")
