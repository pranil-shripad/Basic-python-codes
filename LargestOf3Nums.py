#Largest of 3 numbers
from datetime import timeit 
def myfunc():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))

    if (n1<n2 and n3<n2):
        print("{} is largest.".format(n2))
    elif (n1<n3 and n2<n3):
        print("{} is lsrgest.".format(n3))
    elif (n2<n1 and n3<n1):
        print("{} is largest.".format(n1))
        