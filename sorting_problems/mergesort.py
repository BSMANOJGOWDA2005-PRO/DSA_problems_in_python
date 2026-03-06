# Merge Sort Implementation
#adding two sorted lists by using merge function
def merge(left , right):
    result = []
    i=j=0
    n,m=len(left),len(right)
    while i < n and j <m:
        if left[i]< right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < n:   #if there are remaining elements in left list then add them to result
        result.append(left[i])
        i += 1
    while j < m:#if there are remaining elements in right list then add them to result
        result.append(right[j])
        j += 1
    print(result)#output: [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
        
    
left = [1,2,3,4]
right=[1,1,3,4,5,6,7]
merge(left,right)

#------------------------------------------------------------------------------------------
# Merge Sort Algorithm
#perform merge sort by using divide and conquer approach
#divide the list into two halves 
#conquer by recursively calling merge sort on both 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)#recursively calling merge sort on left half
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left): #if remainig element in left list add to arr[k]
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):#if remainig element in right list add to arr[k]
            arr[k] = right[j]
            j += 1
            k += 1

arr = [5,1,4,3,1,7,8,2]
merge_sort(arr)
print(arr)