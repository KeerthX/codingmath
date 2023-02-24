def madhava(n):
    pi_value = 0
    for i in range (1,n):
        f = 4*((-1)**(i-1))/(2*i-1)
        pi_value = pi_value + f
    return pi_value

print(madhava(1000)) #Take values above 1000 for values near 3.14
