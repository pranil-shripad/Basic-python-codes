#Fibonacci Series
terms = int(input ("How many terms the user wants to print? "))
n1 = 0
n2 = 1

fib = []
for count in range(terms):  
    fib.append(n1)  
    nth = n1 + n2  
    n1 = n2  
    n2 = nth  
    
print(fib)