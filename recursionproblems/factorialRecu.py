# Factorial of a number using while loop
n = int(input("Enter your factorial number: "))
fac_n=1
i = 1
while i <= n:
    if n == 0 or n == 1:
        fac_n = 1
        break
    fac_n = fac_n * i 
    i += 1
    
print(fac_n)   #output will be 120 for n=5

# Factorial of a number using recursion
def factorial(num):
    if num ==0 or num==1:
        return 1
    return num * factorial(num-1)  # factorial(num-1) itself a function 
    
x=factorial(5)
print(x)    #output will be 120 for n=5S