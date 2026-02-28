# Recursion function by tail recursion
#tail from N to 1
def fun(i,n):
    if i >n:
        return
    fun(i+1,n)
    print(i)      #output will be 5,4,3,2,1
fun(1,5) 


# Recursion function by tail recursion
#tail from 1 to N
def fun(i,n):
    if n<=0:
        return
    fun(i,n-1)
    print(n)  #output will be 1,2,3,4,5

fun(1,5)