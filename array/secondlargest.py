# Python program to find the largest and second largest element in a list
nu =[1,2,3,5,2,55,55]
largest = 0
s_lar = 0
for i in nu:
    if i >largest: #if the current element is greater than the largest element
        s_lar = largest #update the second largest element 
        largest = i #update the largest element
    elif i > s_lar and i != largest: 
        s_lar = i
    
    
print(f"largest element in list is: {largest}")#output: largest element in list is: 55
print(f"second largest is : {s_lar}") #Output: second largest is : 5