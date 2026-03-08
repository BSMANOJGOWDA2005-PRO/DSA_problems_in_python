# Find the largest number in a list of numbers
n = [55,23,-97,99,3,67]
largest =0
for i in n:
    if i > largest:
        largest = i
print(largest) # Output: 99
#Tc: O(n) where n is the number of elements in the list
#Sc: O(1) as we are using only a constant 


#------------------------------------------------------
# Another way to find the largest number in a list of numbers
n = [55,23,-97,90,3,67]
largest = n[0]
m = len(n)
for i in range(0,m):
    largest = max(largest,n[i])
print(largest) # Output: 90
#Tc: O(n) where n is the number of elements in the list
#Sc: O(1) as we are using only a constant