#Factorial of a number
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

num = int(input("Enter a number: "))
print("Factorial of {} is {}".format(num,fact(num)))