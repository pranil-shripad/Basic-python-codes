num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("First number after swapping is {}".format(num1))
print("Second number after swapping is {}".format(num2))
