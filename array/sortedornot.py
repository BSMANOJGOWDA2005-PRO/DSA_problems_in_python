#check list is sorted or not by using flag
n = [1,2,3,4,5,6,7,8,9]
m= len(n)
flag = True
for i in range(0,m-1):
    if n[i]>n[i+1]:
        flag = False
        break
if flag:
    print("sorted")
else:
    print("not sorted")
    
#-----------------------------------------------------------
#check list is sorted or not by using else statement of for loop
n = [1,2,3,4,3,6,7,8,9]
m= len(n)
for i in range(0,m-1):
    if n[i]>n[i+1]:
        print("not sorted")
        break
else:
    print("sorted")
    
