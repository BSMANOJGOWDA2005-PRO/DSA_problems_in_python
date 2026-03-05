#Bubble Sort
def bubble(num):
    n = len(num)  
    for i in range(n-2,-1,-1):# 7-2=5, upto 0, reverse order
        for j in range(0,i+1): #0 t0 i+1
            if num[j]> num[j+1]: 
                num[j], num[j+1] = num[j+1], num[j]
num =[5,6,4,3,7,8,2]
bubble(num)
print(num) #output: [2, 3, 4, 5, 6, 7, 8