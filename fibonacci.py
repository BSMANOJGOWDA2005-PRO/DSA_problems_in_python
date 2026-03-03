# Fibonacci series: 0,1,1,2,3,5,8,13,21,34,55,89,144
#number           : 0,1,2,3,4,5,6,7,8,9,10,11,12 

def func(n):
    if n == 0 or n== 1:
        return n
    return func(n-1)+func(n-2) #f(6)+ f(5)

print(func(7))
         #output will be 13 for n=7
        