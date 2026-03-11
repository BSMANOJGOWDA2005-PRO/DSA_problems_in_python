#check missing number in array
num = [0,1,2,3,4,5,7,8,9,10]#6 is missing
n = len(num)
for i in range(0,n+1):
    if i not in num: #check if i is not in num
        print(i)#output 6
#tc: O(n^2) because we are iterating through the array once and checking membership in a list3
#sc: O(1) because we are not using any extra space



#another way to solve the problem is to use a dictionary 
num = [0,1,2,3,4,5,7,8,9,10]
n= len(num)
result = {}
for i in range(0,n+1):
    result[i]=0 #0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0
    if i in num:
        result[i]=1 #0:1,1:1,2:1,3:1,4:1,5:1,7:1,8:1,9:1,10:1
    else:
        result[i]=0 #6:0
print(result)
for key,values in result.items():
    if values==0:
        print(key)#output 6
#Tc: O(n**2) because for loop o(n) and if statement takes O(n) time + O(n) for key,values in result.items() loop
#Sc: O(n) because we are using a dictionary to store the elements


#another way to solve the problem is to use a dictionary
num = [0,1,2,3,4,5,7,8,9,10]
n= len(num)
result = {}
for i in range(0,n+1):
    result[i]=0
for nums in num:
    result[nums]=1 #0:1,1:1,2:1,3:1,4:1,5:1,7:1,8:1,9:1,10:1
print(result)
for key,values in result.items():
    if values==0:
        print(key)#output 6
#Tc: O(n) 1st for loop + o(n) 2nd for loop+ O(n) key,values in result.items() = O(n) 
#Sc: O(n) because we are using a dictionary to store the elements