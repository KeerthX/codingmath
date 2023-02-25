sequence = []
#This gives the list of all fibonacci numbers upto the entered point 
def lucas(n):
    a = 2
    b = 1
    sequence.append(a)
    sequence.append(b)
    for i in range(0,n-1):
        c = a + b
        a,b = b,c
        sequence.append(c)
    return sequence

#This gives the fibonacci number at the point specified
def nth_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return nth_lucas(n-1) + nth_lucas(n-2)

    

n = 11 #Enter the number 
print(lucas(n)) #Prints list of fibonacci numbers
print(nth_lucas(n)) #Prints the value of fibonacci number at that point 
        
