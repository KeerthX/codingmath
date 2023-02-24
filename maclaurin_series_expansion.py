import sympy as sp 
series = []
x = sp.symbols('x')
def maclaurin_series(f,n):
    
    series = []
    for i in range(0,n):
        derivative = sp.diff(f,x,i)
        coeff = derivative / sp.factorial(i)
        series.append(coeff)
    result = "+".join([str(series[i]) + " x^" + str(i) for i in range(n)])
    return result

f = sp.sin(x) #Use any function within the sympy package for this 
z = maclaurin_series(f,10) #Define upto which point u want to find the maclaurin series
print(z) #Print the series



