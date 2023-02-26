def fact(n): #Defining factorial function for the catalan formula 
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def nth_catalan(n): #gives the nth catalan number
    if n == 0:
        return 1 
    else:
        return int(fact(2*n) / (fact(n+1)*fact(n)))

n = 10
print(nth_catalan(n)) #Prints a single catalan value