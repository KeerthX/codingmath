sequence = []
#This gives the list of all fibonacci numbers upto the entered point 
def fibonacci(n):
    a = 0
    b = 1
    sequence.append(a)
    sequence.append(b)
    for i in range(0,n-1):
        c = a + b
        a,b = b,c
        sequence.append(c)
    return sequence

#This gives the fibonacci number at the point specified
def nth_fib(n):
    if n <= 1:
        return n
    return nth_fib(n-1) + nth_fib(n-2)


n = 11 #Enter the number 
print(fibonacci(n)) #Prints list of fibonacci numbers
print(nth_fib(n)) #Prints the value of fibonacci number at that point 
        
