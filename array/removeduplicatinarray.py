#By using set
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
print(set(num))


#By using list
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
result = []
for i in num:
    if i not in result:
        result.append(i)
print(result)


#By using dictionary
num = [1, 2, 3, 4, 1, 5, 1, 2, 1, 2, 3]
dic = {}
for i in num:
    dic[i]=0
print(dic)