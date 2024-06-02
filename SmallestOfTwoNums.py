#Smallest of two numbers
n1 = int(input("Enter First Num: "))
n2 = int(input("Enter Second num: "))

if n1==n2:
    print("{} is equal to {}".format(n1,n2))
elif n1>n2:
    print("{} is smaller than {}".format(n2,n1))
else:
    print("{} is smaller than {}".format(n1,n2))