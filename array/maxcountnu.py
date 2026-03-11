# Count the maximum number of consecutive 1's in an array of 0's and 1's.
num = [1,1,1,1,1,0, 1, 0, 1, 1, 1, 1, 0]
n = len(num)
count = 0
max_count = 0
for i in num:
     if i==1:
         count +=1
         max_count = max (max_count, count)#max(5,4)
     else:
         count = 0
print(max_count)#output:5
# Time complexity: O(n) where n is the length of the input array.
# Space complexity: O(1) since we are using only a


