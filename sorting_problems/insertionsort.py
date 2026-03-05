# Insertion Sort Algorithm
def insertion(num):
    n = len(num)
    for i in range (1,n):
        key = num[i]  #initially key is 6
        j = i-1   #initially j is 0 because i is 1
        while j >= 0 and num[j] > key: 
            num[j+1] = num[j] #shift the number to the right
            j = j-1  #decrease j by 
        num[j+1] = key  #place the key in its correct position in the sorted subarray
        
num =[5,6,4,3,7,8,2]
insertion(num)
print(num) #output: [2, 3, 4, 5, 6, 7, 8]