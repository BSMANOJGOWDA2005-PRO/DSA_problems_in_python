n = 1234567
num = n
count =0
while num>0:
    print(num%10)
    num = num//10
    count+=1
print(f"total count of digits is {count}")