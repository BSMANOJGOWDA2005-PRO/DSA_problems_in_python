# Selection Sort Algorithm

def selection(num):
    n = len(num)  #length of the list is(6)
    for i in range(0, n):  #i= [5,6,4,3,7,8,2]
        min_in=i  #min initially 5
        for j in range(i+1, n): #j= [6,4,3,7,8,2]
            if num[j]< num[min_in]: #6<5, 4<5=T, 3<5=T, 7<5, 8<5, 2<5+t
                min_in=j  #min_in= 2
        num[i], num[min_in] = num[min_in], num[i] #swap 5 with 2
        #6 with 3, 4 with 4, 3 with 6, 7 with 7, 8 with 8
num =[5,6,4,3,7,8,2]
selection(num)
print(num)
