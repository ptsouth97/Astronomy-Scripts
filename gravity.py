import constants
''' Enter masses and radius in scientific notation form'''
G=constants.G
m1=float(input("m1= "))
e1=float(input("e1= "))
m2=float(input("m2= "))
e2=float(input("e2= "))
r=float(input("r= "))
e3=float(input("e3= "))
F=G*(m1*10**e1)*(m2*10**e2)/(r*10**e3)**2
print("Force = "+str(F)+"N")
