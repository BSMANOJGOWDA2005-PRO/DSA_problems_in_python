# Recursion is a function that calls itself
#Head recursion 
count = 0
def name():
    global count
    if count == 4:
        return     # return wiil stop the function from calling itself
                   # retuen values are store in the like result = name() 
                   #  result will be store values 
    print("manoj")
    count += 1
    name()
    
name()


#Tail recursion

count = 0
def name():
    global count
    if count == 4:
        return    
    count += 1
    name()
    print("manoj")
    
name()
