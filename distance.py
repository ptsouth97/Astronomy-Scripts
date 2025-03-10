import constants
'''Convert from one distance unit to another'''
value=float(input("What is the value to be converted?  "))
x=input("Convert from: m, AU, ly, pc:  ")
y=input("Convert to: m, AU, ly, pc:  ")
if(x=='m'):
	if(y=='AU'):
		z=constants.m_AU
	if(y=='ly'):
		z=constants.m_ly
	if(y=='pc'):
		z=constants.m_pc
if(x=='AU'):
	if(y=='m'):
		z=1/constants.m_AU
	if(y=='ly'):
		z=constants.AU_ly
	if(y=='pc'):
		z=constants.AU_pc
if(x=='ly'):
	if(y=='m'):
		z=1/constants.m_ly
	if(y=='AU'):
		z=1/constants.AU_ly
	if(y=='pc'):
		z=constants.ly_pc
if(x=='pc'):
	if(y=='m'):
		z=1/constants.m_pc
	if(y=='AU'):
		z=1/constants.AU_pc
	if(y=='ly'):
		z=1/constants.ly_pc
conversion=value/z
print("The converted value is "+str(conversion)+" "+y)
