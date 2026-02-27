n =153
num = n
total =0
while num > 0:
    last= num%10                        # 153%10 = 3, 15%10 = 5, 1%10 = 1
    total = total + last * last * last  # 0 + 3*3*3 + 5*5*5 + 1*1*1
    num = num//10                        #153//10 = 15, 15//10 = 1, 1//10 = 0
print(f"total is :{total}")
    