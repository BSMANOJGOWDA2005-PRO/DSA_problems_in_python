# Reversing a list using recursion
def re(n,lef,right):
    if lef>=right:  
        return
    n[lef],n[right]=n[right],n[lef]  #swapping  a,b = b,a
    re(n,lef+1,right-1)   #recursive call for next left increment and right decrement

n = [1,2,3,4,5]
re(n,0,len(n)-1)  #n is the list, 0 is left index and len(n)-1 is right index 5-1=4[0,4]
print(n) #output will be [5,4,3,2,1]

#------------------------------------------------------


# Reversing a list using reverse() method
l = [ 1,2,3,4,5,6,7,8,9,10]
l.reverse()
print(l) #output will be [10,9,8,7,6,5,4,3,2,1]


#---------------------------------------------------------
# Reversing a list using the built-in reversed() function
l = [ 1,2,3,4,5,6,7,8,9,10]
result = reversed(l)
print(list(result)) 


#---------------------------------------------------------
# Reversing a list using slicing
l =[ 1,2,3,4,5,6,7,8,9,10]
result = l[::-1]
print(result)

