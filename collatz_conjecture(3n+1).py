sequence = [0]
import matplotlib.pyplot as plt

def conj_collatz(n): #This functions gives the values of the collatz conjecture 
    while n!= 1:
        # print(n)
        if (n % 2 == 0):
            n = n //2
        else:
            n = n*3 + 1
        sequence.append(n)
    print(sequence)
    return sequence

def plot_collatz(n): #This functions gives the plots of the collatz conjecture 
    conj_collatz(n)
    x = range(len(sequence))
    plt.plot(x, sequence)
    plt.show()

n=27435
conj_collatz(n)
plot_collatz(n)


