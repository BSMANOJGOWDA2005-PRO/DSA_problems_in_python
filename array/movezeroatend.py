# Move all the 0's to the end of the list
num = [1,2,3,0,0,7,6,0,4,5,6,7]
n = len(num)
result = []
for i in num: 
    if i != 0:
        result.append(i)
for i in num:
    if i == 0:
        result.append(i)
print(result)# Output: [1, 2, 3, 7, 6, 4, 5, 6, 7, 0, 0, 0]


#--------------------------------------------------------------
#add 0 at the end of the list
num = [1,2,3,0,0,7,6,0,4,5,6,7]
j = 0
for i in range(len(num)):
    if num[i] != 0:
        num[i], num[j] = num[j], num[i]#swap the non-zero element with the element at index j
        j += 1

print(num)# Output: [1, 2, 3, 7, 6, 4, 5, 6, 7, 0, 0, 0]