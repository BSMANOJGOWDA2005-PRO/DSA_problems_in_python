list1=[1,3,2,5,4,4,3,3,1,2,3,11]
list2=[1,2,3,4,5,6,7,8,9,0]

result = {}

for num in list1:
    if num in list2:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

print(result)
