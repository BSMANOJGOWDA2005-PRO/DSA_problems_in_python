num = [1,2,3,4,5,6,21,1,3,4,4,3,2,1,2,3,4,]

dictionary = {}
for i in num:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)






#By using counter
from collections import Counter
n = [5,6,7,1,11,1,1,5,1,1,4,5,6,7,9]
print(Counter(n))


# output:{1: 3, 2: 3, 3: 4, 4: 4, 5: 1, 6: 1, 21: 1}