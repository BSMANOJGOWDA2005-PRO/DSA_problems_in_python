# This code finds pairs of numbers in the list that add up to a target value (17 in this case).
num = [5,9,1,2,4,15,6,3]
n = len(num)
target = 17
for i in range(n):
    for j in range(i+1, n):
        if num[i] + num[j] == target:# If the sum of the two numbers equals the target, print the pair.
            print(f"{num[i]} + {num[j]} = {target}")