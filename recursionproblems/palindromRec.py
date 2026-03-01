# palindrome using recursion
def func(n,l,r):
    if l>=r:
        return True
    if n[l]!=n[r]:
        return False
    return func(n,l+1,r-1)   # ✅ return added

s = "malayalam"

if func(s, 0, len(s)-1):
    print("It's a palindrome")
else:
    print("It's not a palindrome")


#-----------------------------------------------


#palindrome using while loop
n ='malayalam'
left = 0
rigth=len(n)-1

while left < rigth:
    if n[left]!= n[rigth]:
        print("its not a palindrom")
        break
    left +=1
    rigth -=1
else:
    print("its palindrom")
    
#-----------------------------------------------
#palindrome using slicing
name = "malayalam"
reverse_name = name[::-1]
if name == reverse_name:
    print("It's a palindrome")
else:
    print("It's not a palindrome")