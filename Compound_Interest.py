# Compound interest
p = int(input('Enter Principle: '))
r = int(input("Enter rate of interest: "))
t = int(input('Enter Time period: '))
n = int(input("Enter number of times interest is compounded per year: "))

Ci = (p*(1+(r/100))**(n*t))- p

print("Compound interest is: ",Ci)