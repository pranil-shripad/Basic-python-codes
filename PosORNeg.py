#Check if number is +ve or -ve
num = int(input("Enter a number: "))
if num<0:
    print("{} is negative number.".format(num))
elif num > 0 :
    print("{} is positive number.".format(num))
else:
    print("Number is zero.")