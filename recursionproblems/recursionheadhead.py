#recursion function by Head from 1 t0 N
def fun(i,n):
    if i>n:
        return
    print(i)   #output will be 1,2,3,4,5
    fun(i+1,n)
fun(1,5)

#recursion function by Head from N to 1
def fun(i,n):
    if n<i:
        return
    print(n)     #output will be 5,4,3,2,1
    fun(i,n-1)
fun(1,5)