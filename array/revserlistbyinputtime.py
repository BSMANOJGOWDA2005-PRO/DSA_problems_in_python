# Reverse list by input time
n = [1,2,3,4,5,6]
k = 3 # number of times we want to rotate the list
while k>0:
    e = n.pop() # pop() will remove the last element of the list 
    n.insert(0,e) #insert() will insert the element at the specified index
    k-=1
print(n)# Output: [4, 5, 6, 1, 2, 3]


#-------------------------------------------------------------
# Reverse list by input time without using pop() and insert()
n = [1,2,3,4,5,6,7,8,9]
def reverse(n,left,right):
    while left<right:
        n[left],n[right]=n[right],n[left]
        left+=1
        right-=1
reverse(n,2,7)
print(n)
        